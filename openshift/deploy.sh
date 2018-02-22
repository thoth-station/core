#!/usr/bin/env bash

set -x

#oc cluster up
oc new-project thoth-frontend
oc new-project thoth-middleend
oc new-project thoth-backend
oc process -f template.yaml | oc apply -f -

# Deploy Gremlin for a local setup
oc project thoth-middleend
[ "${THOTH_LOCAL}" = 1 ] && oc process -f gremlin.yaml | oc apply -f -
