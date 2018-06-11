#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# thoth-core
# Copyright (C) 2018 Christoph Görn
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
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A scrum helper bot."""


import os
import logging

import requests

from thoth.common import init_logging


class InvalidPayload(Exception):
    pass


class HTTPError(Exception):
    pass

__version__ = '0.1.0'


DEBUG = bool(os.getenv('DEBUG', False))

SERVER_URL = os.getenv('SESHETA_SERVER_URL', 'https://chat.openshift.io')
TEAM_ID = os.getenv('SESHETA_TEAM_ID', 'aicoe')
ENDPOINT_URL = os.getenv('SESHETA_ENDPOINT_URL', None)
BOT_MESSAGE = os.getenv('SESHETA_BOT_MESSAGE', None)

init_logging()
_LOGGER = logging.getLogger('thoth.core.bots.daily_standup')

if DEBUG:
    _LOGGER.setLevel(level=logging.DEBUG)
else:
    _LOGGER.setLevel(level=logging.INFO)


if __name__ == '__main__':
    _LOGGER.info(f'Thoth Core Bot: Daily Standup Helper v{__version__}')

    if ENDPOINT_URL is None:
        _LOGGER.error('No Mattermost incoming webhook URL supplied!')
        exit(-1)

    if BOT_MESSAGE is None:
        _LOGGER.error('No bot message supplied!')
        exit(-2)

    payload = {'text': BOT_MESSAGE,
               'icon_url': 'https://avatars1.githubusercontent.com/u/33906690'}

    r = requests.post(ENDPOINT_URL, json=payload)
    if r.status_code != 200:
        raise HTTPError(r.text)
