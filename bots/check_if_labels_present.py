#!/usr/bin/env python3

import os
import logging
import yaml

from github import Github
from github import UnknownObjectException

from thoth.common import init_logging


__module__ = 'thoth.bots.check_if_labels_present'
__version__ = '0.2.0'

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

    DEFAULT_LABELS = [
        {'name': 'testing', 'color': 'c0c0c0'}
    ]

else:
    with open("config.yaml", 'r') as config:
        RUNTIME_CONFIG = yaml.load(config)

    GITHUB_ORGANIZATION = RUNTIME_CONFIG['organization']
    GITHUB_REPOSITORIES = RUNTIME_CONFIG['repositories']
    DEFAULT_LABELS = RUNTIME_CONFIG['defaultLabels']

    org = github.get_organization(GITHUB_ORGANIZATION)

if org is None:
    _LOGGER.error('Can not get a Github Organization or User...')
    exit(-2)

core = org.get_repo(GITHUB_REPOSITORIES[0])

_LOGGER.info(
    f"Hi, I'm {github.get_user().name}, and I'm fully operational now!")


def ensure_label_present(repo, label_name, label_color, current_labels):
    present_labels = []

    for label in current_labels:
        present_labels.append(label.name)

    if label_name not in present_labels:
        _LOGGER.info(f"adding '{label_name}' label to {repo.name}")

        try:
            repo.create_label(label_name, label_color)

        except UnknownObjectException as e:
            _LOGGER.error(e)

            repo.create_issue(f"can't create '{label_name}' label")
            _LOGGER.info('issue created!')
    else:
        _LOGGER.info(f"label '{label_name}' was present")


if __name__ == '__main__':
    for repo in GITHUB_REPOSITORIES:
        _LOGGER.info(
            f"checking if all required labels are present in repository {repo}")

        _repo = org.get_repo(repo)
        current_labels = _repo.get_labels()

        for label in DEFAULT_LABELS:
            _LOGGER.info(f"checking for '{label['name']}'")
            ensure_label_present(
                _repo, label['name'], label['color'], current_labels)
