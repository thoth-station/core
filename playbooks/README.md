# Thoth's Ops Secrets

This is a containerized version of the Ansible playbooks used to operate Thoth. They are containerized to provide a stable Ansible environment, keeping all its modules up to date and well integrated is not that easy all the time.

Base is a Fedora 28 container image, and the Thoth Ops Container Image is build using buildah. If you want you can run it with #nobigdatdaemon and just podman!

## Build the Ops Container Image

`./build-ops-container-image.sh`

## Running an Ops Playbook

### Prerequisites

`oc login https://paas.upshift.redhat.com --token=z-y-x`

### Bootstrap the STAGE environment

```bash
sudo podman run -ti thoth-ops-container ansible-playbook --extra-vars token=$(oc whoami --show-token) playbooks/bootstrap_stage_upshift.yaml
```