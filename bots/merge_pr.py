#!/usr/bin/env python3

import os
import logging
import yaml

from github import Github
from github import UnknownObjectException

from thoth.common import init_logging


__module__ = 'thoth.bots.check_if_labels_present'
__version__ = '0.1.0-dev'

DEBUG = bool(os.getenv('DEBUG', False))
TEST = bool(os.getenv('TEST', False))
SESHETA_GITHUB_ACCESS_TOKEN = os.getenv('SESHETA_GITHUB_ACCESS_TOKEN', None)

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

init_logging()
_LOGGER = logging.getLogger(__module__)  # pylint: disable=invalid-name

_LOGGER.info(f"Version v{__version__}")

if SESHETA_GITHUB_ACCESS_TOKEN is None:
    _LOGGER.error(
        'Github Token not provided via environment variable SESHETA_GITHUB_ACCESS_TOKEN')
    exit(-1)

github = Github(SESHETA_GITHUB_ACCESS_TOKEN)

if TEST:
    GITHUB_REPOSITORIES = ['bots-playground']

    org = github.get_user('goern')
else:
    with open("config.yaml", 'r') as config:
        RUNTIME_CONFIG = yaml.load(config)

    GITHUB_ORGANIZATION = RUNTIME_CONFIG['organization']
    GITHUB_REPOSITORIES = RUNTIME_CONFIG['repositories']

    org = github.get_organization(GITHUB_ORGANIZATION)

if org is None:
    _LOGGER.error('Can not get a Github Organization or User...')
    exit(-2)


_LOGGER.info(
    f"Hi, I'm {github.get_user().name}, and I'm fully operational now!")


if __name__ == '__main__':

    for _repo in GITHUB_REPOSITORIES:
        _LOGGER.info(
            f"checking '{org.login}/{_repo}' for 'approved' Pull Requests")
        repo = org.get_repo(_repo)

        for pr in repo.get_pulls(state='open'):
            if pr.mergeable:
                merge_it = False
                labels = []

                _LOGGER.info(f"maybe merge {pr.id}")

                try:
                    labels = pr.as_issue().get_labels()
                except AttributeError as e:
                    _LOGGER.error(e)

                for label in labels:
                    if label.name == 'approved':
                        merge_it = True

                    if (label.name == 'do-not-merge') or (label.name == 'work-in-progress'):
                        merge_it = False

                if merge_it:
                    _LOGGER.info(f"let's do it! merging {pr.id}")

                    merged = pr.merge()

                    _LOGGER.info(f"{pr.id} {merged.message}")
                else:
                    _LOGGER.info(f"not merging {pr.id}")
