#!/usr/bin/env bash

set -ex

#oc cluster up
oc new-project thoth-frontend
oc new-project thoth-middleend
oc process -f template.yaml | oc apply -f -
oc project thoth-frontend
