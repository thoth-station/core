#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   thoth-core
#   Copyright(C) 2018 Christoph Görn
#
#   This program is free software: you can redistribute it and / or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Thoth: Core: End-to-End Tests: User API feature test steps."""

import time

from http import HTTPStatus

import requests

from behave import given, when, then
from hamcrest import assert_that, equal_to, is_not, not_none, less_than


@when(u'I submit {a_container_image} to the User API for analysis by {analyser_image}')
def step_impl(context, a_container_image, analyser_image):
    payload = {
        'image': a_container_image,
        'analyzer': analyser_image
    }

    r = requests.post(f'{context.endpoint_url}/analyze', params=payload)

    assert_that(r.status_code, equal_to(HTTPStatus.ACCEPTED))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    response = r.json()
    assert_that(response, not_none)
    context.response = response


@when(u'I query the Result API for my latest analyser result')
def step_impl(context):
    payload = {
        'pod_id': context.analyzer_job_id
    }
    r = requests.get(
        f'{context.endpoint_url}/log', params=payload)

    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    analyzer_job_log = r.json()
    assert_that(analyzer_job_log, not_none)

    assert_that(analyzer_job_log['pod_id'], equal_to(context.analyzer_job_id))

    context.analyzer_job_log = analyzer_job_log


@then(u'I want to receive a Analyser Job ID')
def step_impl(context):
    assert_that(context.response, not_none)

    analyzer_job_id = context.response['pod_id']
    assert_that(analyzer_job_id, not_none)

    context.analyzer_job_id = analyzer_job_id


@then(u'I wait for the Analyser Job to finish successful')
def step_impl(context):
    time.sleep(15)

    analyzer_job_terminated = False
    analyzer_job_termination_retries = 0

    while not analyzer_job_terminated:
        time.sleep(5)

        payload = {
            'pod_id': context.analyzer_job_id
        }
        r = requests.get(
            f'{context.endpoint_url}/status', params=payload)

        assert_that(r.status_code, equal_to(HTTPStatus.OK))
        assert_that(r.headers['content-type'], equal_to('application/json'))

        response = r.json()
        assert_that(response, not_none)

        if 'terminated' in response['status'].keys():
            if response['status']['terminated']['reason'].startswith('Completed'):
                analyzer_job_terminated = True

        analyzer_job_termination_retries += 1

        assert_that(analyzer_job_termination_retries, less_than(10))


@then(u'the Analyzer Job Log should not be empty')
def step_impl(context):
    payload = {
        'pod_id': context.analyzer_job_id
    }
    r = requests.get(
        f'{context.endpoint_url}/log', params=payload)

    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    analyzer_job_log = r.json()
    assert_that(analyzer_job_log, not_none)

    assert_that(analyzer_job_log['pod_id'], equal_to(context.analyzer_job_id))
