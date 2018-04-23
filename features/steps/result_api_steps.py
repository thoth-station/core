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

"""Thoth: Core: End-to-End Tests: Result API feature tests."""

from http import HTTPStatus

import requests

from behave import given, when, then
from hamcrest import assert_that, equal_to, is_not, not_none


@given('I am using the TEST environement')
def step_impl(context):
    # TODO read this from ENV
    context.endpoint_url = 'http://user-api-thoth-test-core.cloud.upshift.engineering.redhat.com/api/v1/analyze'


@when('I query the Result API for a list of analyser results')
def step_impl(context):
    r = requests.get(context.endpoint_url)

    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    result_list = r.json()
    assert_that(result_list, not_none)
    context.result_list = result_list['results']


@when('I get one of the results')
def step_impl(context):
    assert_that(len(context.result_list), not equal_to(0))

    # TODO this could be a little bit more random choice
    context.chosen_result = context.result_list[0]

    r = requests.get(f'{context.endpoint_url}/{context.chosen_result}')
    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    chosen_result_json = r.json()
    assert_that(chosen_result_json, not_none)
    context.chosen_result_json = chosen_result_json


@then('the list of analyser results should not be empty')
def step_impl(context):
    assert_that(len(context.result_list), not equal_to(0))


@then('the analyser result should not be empty')
def step_impl(context):
    assert_that(context.chosen_result, not_none)


@then('the analyser should be "{name}"')
def step_impl(context, name):
    assert_that(context.chosen_result_json['metadata']['analyzer'],
                equal_to(name))


@then('the analyser version should be "{version}"')
def step_impl(context, version):
    assert_that(context.chosen_result_json['metadata']['analyzer_version'],
                equal_to(version))
