#!/usr/bin/env bash

set -ex

oc cluster up
oc login -u system:admin
oc process -f template.yaml | oc apply -f -
oc login -u developer -p developer
oc project thoth-frontend
