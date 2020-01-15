#!/usr/bin/env python
# thoth-core
# Copyright(C) 2018, 2019, 2020 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Thoth: Core: End-to-End Tests: User API feature test steps."""

import time

from http import HTTPStatus

import requests

from behave import given, when, then
from hamcrest import assert_that, equal_to, is_not, not_none, less_than


@when('I submit {a_container_image} to the User API for analysis by {analyzer_image}')
def step_impl(context, a_container_image, analyzer_image):
    payload = {
        'image': a_container_image,
        'analyzer': analyzer_image
    }

    r = requests.post(f'{context.endpoint_url}/analyze', params=payload)

    assert_that(r.status_code, equal_to(HTTPStatus.ACCEPTED))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    response = r.json()
    assert_that(response, not_none)
    context.response = response


@then('I want to receive a analyzer Job ID')
def step_impl(context):
    assert_that(context.response, not_none)

    analyzer_job_id = context.response['pod_id']
    assert_that(analyzer_job_id, not_none)

    context.analyzer_job_id = analyzer_job_id


@then('I wait for the analyzer Job to finish successful')
def step_impl(context):
    time.sleep(15)
    analyzer_job_terminated = False
    analyzer_job_termination_retries = 0

    while not analyzer_job_terminated:
        time.sleep(10)

        analyzer_job_id = context.response['pod_id']
        r = requests.get(f'{context.endpoint_url}/status/{analyzer_job_id}')

        assert_that(r.status_code, equal_to(HTTPStatus.OK))
        assert_that(r.headers['content-type'], equal_to('application/json'))

        response = r.json()
        assert_that(response, not_none)

        if 'terminated' in response['status'].keys():
            if response['status']['terminated']['reason'].startswith('Completed'):
                analyzer_job_terminated = True

        analyzer_job_termination_retries += 1

        assert_that(analyzer_job_termination_retries, less_than(10))


@then('the Analyzer Job Log should not be empty')
def step_impl(context):
    analyzer_job_id = context.response['pod_id']
    r = requests.get(
        f'{context.endpoint_url}/log/{analyzer_job_id}')

    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    analyzer_job_log = r.json()
    assert_that(analyzer_job_log, not_none)
