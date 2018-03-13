#!/usr/bin/env bash

set -x

. conf.sh

if [ \( "${THOTH_LOCAL}" \) -a -z "${THOTH_ROUTING_SUFFIX}" ]; then
	THOTH_ROUTING_SUFFIX=`ip a | grep inet |grep docker | head -1 | sed 's#.* \([^/]*\)/.*#\1#'`
	THOTH_ROUTING_SUFFIX="${THOTH_ROUTING_SUFFIX}.nip.io"
fi

if [ ! "${THOTH_ROUTING_SUFFIX}" ]; then
	echo "No routing suffix configured for deployment" >&2
	exit 1
fi

[ \( "${THOTH_LOCAL}" \) ] && oc cluster up --routing-suffix="${THOTH_ROUTING_SUFFIX}"
oc new-project thoth-frontend
oc new-project thoth-middleend
oc new-project thoth-backend
oc process -f template.yaml \
	-p THOTH_ROUTING_SUFFIX="${THOTH_ROUTING_SUFFIX}" \
        -p THOTH_DEPLOYMENT_NAME=${THOTH_DEPLOYMENT_NAME} \
        -p THOTH_CEPH_KEY_ID=${THOTH_CEPH_KEY_ID} \
        -p THOTH_CEPH_SECRET_KEY=${THOTH_CEPH_SECRET_KEY} \
        -p THOTH_CEPH_HOST=${THOTH_CEPH_HOST} \
	| oc apply -f -
oc project thoth-middleend
curl https://raw.githubusercontent.com/goern/janusgraph-openshift/master/template.yaml -o janusgraph.yaml
oc process -f janusgraph.yaml | oc apply -f -
