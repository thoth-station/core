#!/usr/bin/env python
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

"""Thoth: Core: End-to-End Tests: Result API feature test steps."""

from http import HTTPStatus

import requests

from behave import given, when, then
from hamcrest import assert_that, equal_to, is_not, not_none, has_items


@when(u'I query the naming service for solver image')
def step_impl(context):
    context.naming_service_endpoint_url = 'http://naming-service-thoth-test-core.cloud.upshift.engineering.redhat.com/api/v0alpha0'

    r = requests.get(f'{context.naming_service_endpoint_url}/solvers')

    assert_that(r.status_code, equal_to(HTTPStatus.OK))
    assert_that(r.headers['content-type'], equal_to('application/json'))

    solvers = r.json()
    assert_that(solvers['items'], not_none)
    context.solvers = solvers['items']


@then(u'I want will get at least the following results')
def step_impl(context):
    solvers = context.solvers

    expected_solvers = [row["name"] for row in context.table]
    actual_solvers = []

    for solver in solvers:
        actual_solvers.append(solver['metadata']['name'])

    assert_that(has_items(*expected_solvers), actual_solvers)
