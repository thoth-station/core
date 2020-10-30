Thoth Operations
================

The following sections describe how we would like to handle certain
categories of components of applications deployed on OpenShift.

We focus on provision/deprovision use cases first. Later additions to
this document may take other operational aspects into account.

Builder ImageStreams
--------------------

Builder ImageStreams are considered common requirements. They should not
be created or deleted by an application (de)provisioning playbook. A
provision playbook should use the ansible role
`thoth-core-imagestreams <https://galaxy.ansible.com/thoth-station/thoth-core-imagestreams>`__
to set up Builder ImageStreams.

Application Components
----------------------

Application Components, such as Deployments, ImageStreams, CronJobs,
should be created and deleted by (de)provision playbooks. Both should be
idempotent.

Persistent Volumes and their Claims
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If persistent volumes are required by an application the corresponding
Persistant Volume Claims should be created by the provision playbook,
but not be removed by the deprovision playbook. We want to preserve any
data that has been created!

If a Persistent Volume Claim already exists, it must not be changed by
the provision playbook.

OpenShift Templates
-------------------

OpenShift Template should be created for

-  Application ImageStreams
-  Application components needed for deployment
-  Application components needed for building

All OpenShift objects must carry application and component labels.

Example:
~~~~~~~~

.. code:: yaml

      - apiVersion: v1
        kind: BuildConfig
        metadata:
          name: adviser
          labels:
            app: thoth
            component: adviser
        spec:
         ...

The meta data for the OpenShift Template itself must carry more
annotations:

.. code:: yaml

    apiVersion: v1
    kind: Template
    metadata:
      name: adviser-buildconfig
      annotations:
        description: This is Thoth Adviser BuildConfig...
        openshift.io/display-name: Thoth Adviser BuildConfig
        tags: poc,thoth,ai-stacks,adviser
        template.openshift.io/documentation-url: https://github.com/Thoth-Station
        template.openshift.io/long-description: This is...
        template.openshift.io/provider-display-name: Red Hat, Inc.
      labels:
        template: adviser-buildconfig
        app: thoth
        component: adviser