#!/bin/bash -xe
# Copyright (C) 2018 Christoph Görn
#

[ -z "$SUDO_COMMAND" ] && exec sudo $0

if ! type buildah; then
    dnf install -y buildah
fi

ctr=$(buildah from registry.fedoraproject.org/fedora:28)
mnt=$(buildah mount $ctr)

## Install dependencies
buildah run $ctr -- dnf update -y
buildah run $ctr -- dnf install -y ansible
buildah run $ctr -- pip install openshift

# Cleanup
buildah run $ctr -- dnf clean all
buildah run $ctr -- rm -Rf /root/.cache

# Setup user environment
buildah run $ctr -- useradd -m thoth-ops

# Copy the playbooks and roles
mkdir -p $mnt/home/thoth-ops/playbooks
cp . -r $mnt/home/thoth-ops/playbooks/
cp $(which oc) /home/thoth-ops/
buildah run $ctr -- chown -R thoth-ops:thoth-ops /home/thoth-ops
buildah run $ctr -- chmod 750 /home/thoth-ops/oc

## Include some buildtime annotations
buildah config --annotation "ninja.thoth-station.build.host=$(uname -n)" $ctr
buildah config --author goern@redhat.com $ctr
buildah config --cmd "/bin/bash" $ctr
buildah config --workingdir /home/thoth-ops $ctr
buildah config --user thoth-ops $ctr

## Commit this container to an image name
buildah umount $ctr
buildah commit $ctr thoth-ops-container
