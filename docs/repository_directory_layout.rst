Repository Directory Layout
===========================

This section describes to directory layout common to all the Thoth-Station repositories.

OpenShift Templates
-------------------

The `openshift/` directory shall contain all the OpenShift template files. These may be processed by Ansible Playbooks
or used directly by humans using `oc apply -f ...`.

This directory also contains OpenShift Templates to create Argo Workflows.

Ansible Playbooks
-----------------

The `ansible/` directory contains all files related to Ansible Playbooks, Roles and other files like variable files.

Argo Workflows
--------------

Argo WorkflowTemplates shall be present in the `workflows/templates/` directory, Argo Workflows (in opposite to an
OpenShift Template creating an Argo Workflow) shall be present in the `workflows/` directory.
