#!/usr/bin/env bash

set -x

# Secret for deployment interaction:
export THOTH_SECRET="secret"

export THOTH_LOCAL=1
# In case you want to deploy to a cluster, comment out the line above and provice routing suffix of the cluster:
#export THOTH_ROUTING_SUFFIX=mycluster.redhat.com

# Adjust if you deploy to actual cluster - this is a namespace to separate different deployments:
export THOTH_DEPLOYMENT_NAME="local-$USER"

# Credentials provided by DataHub team go here:
export THOTH_CEPH_SECRET_KEY=
export THOTH_CEPH_KEY_ID=
export THOTH_CEPH_HOST=
