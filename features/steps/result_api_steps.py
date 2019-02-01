#!/usr/bin/env python
# thoth-core
# Copyright(C) 2018, 2019 Christoph Görn
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

"""Thoth: Core: End-to-End Tests: Result API feature test steps."""

from http import HTTPStatus

import requests

from behave import given, when, then
from hamcrest import assert_that, equal_to, is_not, not_none


@given('I am using the TEST environement')
def step_impl(context):
    # TODO read this from ENV
    context.endpoint_url = 'http://user-api-thoth-test-core.cloud.paas.upshift.redhat.com/api/v1'


@when('I query the Result API for a list of analyzer results')
def step_impl(context):
    r = requests.get(f'{context.endpoint_url}/analyze')

    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    result_list = r.json()
    assert_that(result_list, not_none)
    context.result_list = result_list['results']


@when('I query the Solver API for a list of solver results')
def step_impl(context):
    r = requests.get(f'{context.endpoint_url}/solve')

    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    result_list = r.json()
    assert_that(result_list, not_none)
    context.result_list = result_list['results']


@when('I get one of the analyzer results')
def step_impl(context):
    assert_that(len(context.result_list), not equal_to(0))

    # TODO this could be a little bit more random choice
    context.chosen_result = context.result_list[0]

    r = requests.get(f'{context.endpoint_url}/analyze/{context.chosen_result}')
    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    chosen_result_json = r.json()
    assert_that(chosen_result_json, not_none)
    context.chosen_result_json = chosen_result_json


@when('I get one of the solver results')
def step_impl(context):
    assert_that(len(context.result_list), not equal_to(0))

    # TODO this could be a little bit more random choice
    context.chosen_result = context.result_list[len(context.result_list)-1]

    r = requests.get(f'{context.endpoint_url}/solve/{context.chosen_result}')
    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    chosen_result_json = r.json()
    assert_that(chosen_result_json, not_none)
    context.chosen_result_json = chosen_result_json


@then('I query the Result API for the result of the latest analyzer')
def step_impl(context):
    analyzer_job_id = context.response['pod_id']
    r = requests.get(
        f'{context.endpoint_url}/analyze/{context.analyzer_job_id}')

    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))
    analyzer_result_json = r.json()
    assert_that(analyzer_result_json, not_none)
    context.latest_analyzer_result = analyzer_result_json


@then('the list of results should not be empty')
def step_impl(context):
    assert_that(len(context.result_list), not equal_to(0))


@then('the result should not be empty')
def step_impl(context):
    assert_that(len(context.chosen_result), not equal_to(0))


@then('the analyzer should be "{name}"')
def step_impl(context, name):
    assert_that(context.chosen_result_json['metadata']['analyzer'],
                equal_to(name))


@then('the analyzer version should not be empty')
def step_impl(context):
    assert_that(
        len(context.chosen_result_json['metadata']['analyzer_version']), not equal_to(0))


@then('the solver should be "{name}"')
def step_impl(context, name):
    assert_that(context.chosen_result_json['metadata']['analyzer'],
                equal_to(name))


@then('the solver version should not be empty')
def step_impl(context):
    assert_that(
        len(context.chosen_result_json['metadata']['analyzer_version']), not equal_to(0))


@then('the list of analzer results should not be empty')
def step_impl(context):
    assert_that(len(context.latest_analyzer_result['result']), not equal_to(0))
