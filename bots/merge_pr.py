#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# thoth-core
# Copyright(C) 2018 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>./env python3


"""This will merge PR"""

import os
import logging

import daiquiri
import sesheta

from github import Github
from github import UnknownObjectException

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

from sesheta.common import CICD_CONTEXT_ID, DO_NOT_MERGE_LABELS, get_labels_from_pr, commit_was_successful_tested, init_github_interface


DEBUG = bool(os.getenv('DEBUG', False))
SESHETA_GITHUB_ACCESS_TOKEN = os.getenv('SESHETA_GITHUB_ACCESS_TOKEN', None)
SESHETA_PROMETHEUS_PUSH_GATEWAY = os.getenv(
    'PROMETHEUS_PUSH_GATEWAY', 'pushgateway.thoth-test-core.svc:9091')

prometheus_registry = CollectorRegistry()
_METRIC_MERGED_PULLREQUESTS = Gauge(
    'pullrequests_merged', 'Pullrequests merged', registry=prometheus_registry)

daiquiri.setup(level=logging.INFO)
_LOGGER = daiquiri.getLogger('merger')

if DEBUG:
    _LOGGER.setLevel(level=logging.DEBUG)
else:
    _LOGGER.setLevel(level=logging.INFO)


if __name__ == '__main__':
    if not SESHETA_GITHUB_ACCESS_TOKEN:
        _LOGGER.error(
            'Github Token not provided via environment variable SESHETA_GITHUB_ACCESS_TOKEN')
        exit(-1)

    github, org, GITHUB_ORGANIZATION, GITHUB_REPOSITORIES, DEFAULT_LABELS = init_github_interface(
        SESHETA_GITHUB_ACCESS_TOKEN)

    _LOGGER.info(
        f"Hi, I'm {github.get_user().name}, and I'm fully operational now!")
    _LOGGER.debug("... and I am running in DEBUG mode!")

    for _repo in GITHUB_REPOSITORIES:
        _LOGGER.info(
            f"checking Repository '{org.login}/{_repo}' for 'approved' Pull Requests")
        repo = org.get_repo(_repo)

        for pr in repo.get_pulls(state='open'):
            if pr.mergeable:
                merge_it = False
                labels = []

                _LOGGER.debug(
                    f"check if conditions to merge '{pr.title}' are met")

                try:
                    labels = pr.as_issue().get_labels()
                except AttributeError as e:
                    _LOGGER.error(e)

                for label in labels:
                    if label.name == 'approved':
                        merge_it = True

                    if label.name in DO_NOT_MERGE_LABELS:
                        merge_it = False

                if merge_it:
                    _LOGGER.info(
                        f"I am going to merge Pull Request '{pr.title}'... let's do it!")

                    # merged = pr.merge()

                    _METRIC_MERGED_PULLREQUESTS.inc()

                    _LOGGER.info(f"Pull Request '{pr.title}' {merged.message}")

    if SESHETA_PROMETHEUS_PUSH_GATEWAY:
        try:
            push_to_gateway(SESHETA_PROMETHEUS_PUSH_GATEWAY, job='sesheta-merge-pr',
                            registry=prometheus_registry)
        except Exception as e:
            _LOGGER.exception(
                'An error occurred pushing the metrics: {}'.format(str(e)))
