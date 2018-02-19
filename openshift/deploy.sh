#!/usr/bin/env bash

set -x

#oc cluster up
oc new-project thoth-frontend
oc new-project thoth-middleend
oc process -f template.yaml | oc apply -f -
oc project thoth-frontend

# Deploy Gremlin for a local setup
[ "${THOTH_LOCAL}" = 1 ] && oc process -f gremlin.yaml | oc apply -f -
