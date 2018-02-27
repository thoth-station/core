#!/usr/bin/env bash

set -x

DOCKER_IP=`ip a | grep inet |grep docker | head -1 | sed 's#.* \([^/]*\)/.*#\1#'`

oc cluster up --routing-suffix="${DOCKER_IP}.nip.io"
oc new-project thoth-frontend
oc new-project thoth-middleend
oc new-project thoth-backend
oc process -f template.yaml -p DOCKER_IP=${DOCKER_IP} | oc apply -f -
oc project thoth-middleend
oc process -f janusgraph.yaml | oc apply -f -
