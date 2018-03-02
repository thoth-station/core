#!/usr/bin/env bash

set -x

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
oc process -f template.yaml -p THOTH_ROUTING_SUFFIX="${THOTH_ROUTING_SUFFIX}" | oc apply -f -
oc project thoth-middleend
oc process -f janusgraph.yaml | oc apply -f -
