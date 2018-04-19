#!/usr/bin/env python3

import os
import logging
import yaml

from github import Github
from github import UnknownObjectException

from thoth.common import init_logging


__module__ = 'thoth.bots.approve'
__version__ = '0.2.0-dev'

DEBUG = bool(os.getenv('DEBUG', False))
TEST = bool(os.getenv('TEST', False))
SESHETA_GITHUB_ACCESS_TOKEN = os.getenv('SESHETA_GITHUB_ACCESS_TOKEN', None)
CICD_CONTEXT_ID = 'continuous-integration/jenkins/pr-merge'

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


def commit_was_successful_tested(statuses):
    latest_status_id = 0
    rc = False

    for status in statuses:
        if status.context == CICD_CONTEXT_ID:
            _LOGGER.debug(f"{commit} {status}")

            if latest_status_id < status.id:
                if status.state == 'success':
                    rc = True

    return rc


def get_labels_from_pr(pr):
    """extract a list of strings from github.PaginatedList.PaginatedList of github.Label.Label"""
    labels = []

    try:
        _labels = pr.as_issue().get_labels()
        for _label in _labels:
            labels.append(_label.name)
    except AttributeError as e:
        _LOGGER.error(e)

    return labels


if __name__ == '__main__':
    for _repo in GITHUB_REPOSITORIES:
        _LOGGER.info(
            f"checking '{org.login}/{_repo}' for Pull Requests that could be 'approved'")

        repo = org.get_repo(_repo)

        for pr in repo.get_pulls(state='open'):
            _LOGGER.info(pr)

            labels = get_labels_from_pr(pr)

            if pr.title.startswith('WIP') or pr.title.startswith('[WIP]') or ('work-in-progress' in labels):
                _LOGGER.info(
                    f"'{pr.title}' is not mergeable, it's work-in-progress")

                if 'work-in-progress' not in labels:
                    pr.as_issue().add_to_labels('work-in-progress')

                continue

            if not pr.mergeable:
                _LOGGER.info(f"'{pr.title}' is not mergeable!")

                pr.as_issue().add_to_labels('needs-rebase')
                continue

            if pr.mergeable and ('needs-rebase' in labels):
                _LOGGER.info(
                    f"'{pr.title}' is mergeable, removieng 'needs-rebase' label")

                pr.as_issue().remove_from_labels('needs-rebase')

            # if all commits of this PR are CI'd positive, we might approve the PR
            commits = pr.get_commits()
            maybe_approve = False

            for commit in commits:
                statuses = commit.get_statuses()

                if commit_was_successful_tested(statuses):
                    _LOGGER.info(
                        f"commit '{commit}' was successfully tested by {CICD_CONTEXT_ID}")

                    maybe_approve = True

            if maybe_approve:
                _LOGGER.info(
                    f"We are going to approve Pull Request '{pr.title}'")
            else:
                _LOGGER.info(
                    f"Pull Request '{pr.title}' could not be approved")
