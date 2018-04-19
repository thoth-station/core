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
            f"checking '{org.login}/{_repo}' for Pull Requests that could be 'approved'")

        repo = org.get_repo(_repo)

        for pr in repo.get_pulls(state='open'):
            _LOGGER.info(pr)

            if pr.title.startswith('WIP') or pr.title.startswith('[WIP]'):
                _LOGGER.info(
                    f"'{pr.title}' is not mergeable, it's work-in-progress")

                pr.as_issue().add_to_labels('work-in-progress')
                continue

            if not pr.mergeable:
                _LOGGER.info(f"'{pr.title}' is not mergeable!")

                pr.as_issue().add_to_labels('needs-rebase')
                continue

            commits = pr.get_commits()

            for commit in commits:
                statuses = commit.get_statuses()

                for status in statuses:
                    _LOGGER.info(f"{commit} {status}")
