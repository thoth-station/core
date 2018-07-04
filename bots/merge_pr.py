#!/usr/bin/env python3

import os
import logging

import requests

import daiquiri
import sesheta

from github import Github
from github import UnknownObjectException
from github.GithubException import GithubException

from sesheta.common import CICD_CONTEXT_ID, DO_NOT_MERGE_LABELS, get_labels_from_pr, commit_was_successful_tested, init_github_interface


DEBUG = bool(os.getenv('DEBUG', False))
SESHETA_GITHUB_ACCESS_TOKEN = os.getenv('SESHETA_GITHUB_ACCESS_TOKEN', None)
SERVER_URL = os.getenv('SESHETA_SERVER_URL', 'https://chat.openshift.io')
TEAM_ID = os.getenv('SESHETA_TEAM_ID', 'aicoe')
ENDPOINT_URL = os.getenv('SESHETA_ENDPOINT_URL', None)

daiquiri.setup(level=logging.INFO)
logger = daiquiri.getLogger('merger')

if DEBUG:
    logger.setLevel(level=logging.DEBUG)
else:
    logger.setLevel(level=logging.INFO)


class InvalidPayload(Exception):
    pass


class HTTPError(Exception):
    pass


def notify_channel(message):
    payload = {'text': message,
               'icon_url': 'https://avatars1.githubusercontent.com/u/33906690'}

    r = requests.post(ENDPOINT_URL, json=payload)
    if r.status_code != 200:
        raise HTTPError(r.text)

if __name__ == '__main__':
    if not SESHETA_GITHUB_ACCESS_TOKEN:
        logger.error(
            'Github Token not provided via environment variable SESHETA_GITHUB_ACCESS_TOKEN')
        exit(-1)

    if ENDPOINT_URL is None:
        logger.error('No Mattermost incoming webhook URL supplied!')
        exit(-2)

    github, org, GITHUB_ORGANIZATION, GITHUB_REPOSITORIES, DEFAULT_LABELS = init_github_interface(
        SESHETA_GITHUB_ACCESS_TOKEN)

    logger.info(
        f"Hi, I'm {github.get_user().name}, and I'm fully operational now!")
    logger.debug("... and I am running in DEBUG mode!")

    for _repo in GITHUB_REPOSITORIES:
        logger.info(
            f"checking Repository '{org.login}/{_repo}' for 'approved' Pull Requests")
        repo = org.get_repo(_repo)

        for pr in repo.get_pulls(state='open'):
            if pr.mergeable:
                merge_it = False
                labels = []

                logger.debug(
                    f"check if conditions to merge '{pr.title}' are met")

                try:
                    labels = pr.as_issue().get_labels()
                except AttributeError as e:
                    logger.error(e)

                for label in labels:
                    if label.name == 'approved':
                        merge_it = True

                    if label.name in DO_NOT_MERGE_LABELS:
                        merge_it = False

                if merge_it:
                    try:
                        logger.info(
                            f"I am going to merge Pull Request '{pr.title}'... let's do it!")

                        merged = pr.merge()

                        logger.info(f"Pull Request '{pr.title}' {merged.message}")

                        notify_channel(
                            f"Pull Request <a herf='{pr.html_url}'>{pr.title}</a> has been successfully merged :tada:")

                    except HTTPError as e:
                        logger.error(e)
                    except GithubException as e:
                        logger.error(e)
