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
oc new-project ${THOTH_MIDDLEEND_NAMESPACE}
oc new-project thoth-backend
oc process -f template.yaml \
	-p THOTH_ROUTING_SUFFIX="${THOTH_ROUTING_SUFFIX}" \
        -p THOTH_DEPLOYMENT_NAME=${THOTH_DEPLOYMENT_NAME} \
        -p THOTH_CEPH_KEY_ID=${THOTH_CEPH_KEY_ID} \
        -p THOTH_CEPH_SECRET_KEY=${THOTH_CEPH_SECRET_KEY} \
        -p THOTH_CEPH_HOST=${THOTH_CEPH_HOST} \
        -p THOTH_SECRET=${THOTH_SECRET} \
		-p THOTH_MIDDLEEND_NAMESPACE=${THOTH_MIDDLEEND_NAMESPACE} \
		-p THOTH_BACKEND_NAMESPACE=${THOTH_BACKEND_NAMESPACE} \
	| oc apply -f -


# deploy janusgraph server
oc project ${THOTH_MIDDLEEND_NAMESPACE}
oc process -f https://raw.githubusercontent.com/goern/janusgraph-openshift/master/template.yaml | oc apply -f -
