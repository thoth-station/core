Thoth-core
==========

Welcome to the Thoth-core project README file!

The main aim for this project is to provide a deployment for running containers in a fully isolated and safe environment. Thoth-core provides isolation of containers that are run inside a cluster so you can be sure that a container does not communicate to unwanted services, does not communicate to outside world, does not waste your resources and once computation is done, there are freed all used resources. This is especially helpful if you want to run and test untrusted containers or execute potentially vulnerable code in containers. This project will help you transparently do that by offering:

* configurable resource requests
* automatically killing containers after some time so possible infinite loops, CPU consumption or any other malicious operations are restricted
* inspecting pod logs and pod statuses
* parametrize pod deployment
* database adapters for storing computed results safely using JSONs without directly interacting with database with possibly untrusted code
* a network isolation so containers can communicate only with specified services (currently WIP)


Installation
------------

.. code-block:: console

 $ git clone https://github.com/fridex/thoth-core
 $ cd thoth-core/openshift
 $ ./deploy.sh

You can simply ignore the following error (the default user "developer" does not have sufficient rights to create resource quotas for a namespace, this should be set up by cluster administrator in production):

.. code-block:: console

 Error from server (Forbidden): User "developer" cannot create resourcequotas in project "thoth-middleend"

If you would like to deploy Thoth onto a running OpenShift cluster, feel free to use directly OpenShift template.yaml. You need to specify at least specify running JanusGraph host (currently supported only JanusGraph websocket).


The overall architecture
------------------------

The whole deployment is divided into two namespaces (or two OpenShift projects) - ``thoth-frontend`` and ``thoth-middleend``.

.. figure:: https://raw.githubusercontent.com/fridex/thoth-core/master/images/design.png


Thoth-core frontend
###################

The ``thoth-frontend`` is used as a management namespace. Services running in this namespace have assigned a service account for running and managing pods that are available inside the ``thoth-middleend`` part.

A user can interact with the user-facing API (see `it's repo <https://github.com/fridex/thoth-user-api>`_ for API OpenAPI specification). There can be run a pod that runs a container from requested image. The user can adjust environment variables, resource requests and other properties when running a pod.

Besides raw pods, there can be run specialized pods called "analyzers". The goal of this pods is to analyze images for use in the Thoth project. Basically these analyzers are pods that have additional environment variables present (like the result storing API URL).

A pod called `thoth-cleanup-job <https://github.com/fridex/thoth-cleanup-job>`_ is responsible for cleaning up pod objects from etcd. By default, it is run once a week as Kubernetes CronJob. As CronJobs are pure Kubernetes objects, the thoth-cleanup-job is pulled from registry specified on deployment (see the `OpenShift YAML template <https://github.com/fridex/thoth-core/blob/master/openshift/template.yaml>`_) rather than using s2i.


Thoth-core middleend
####################

All pods requested to be run run inside the middleend namespace. There is run the result-storing API service that is responsible for syncing results of pods run in the middleend namespace to a database (as the endpoint accepts textual JSON as an input to the POST request, pods cannot directly interact with the database).


Cluster requirements
--------------------

In order to create NetworkPolicy objects, there needs to be enabled the ``ovs-networkpolicy`` plugin - see `docs for more details <https://docs.openshift.com/container-platform/3.6/admin_guide/managing_networking.html#admin-guide-networking-networkpolicy>`_ and OpenShift 3.5 or newer as NetworkPolicy objects were introduced in starting `OpenShift version 3.5 as a tech preview <https://blog.openshift.com/whats-new-in-openshift-3-5-network-policy-tech-preview/>`_.

As of now, NetworkPolicy is not applied so there are no network restrictions to created pods. This enables pods to reach outside world without any fine-granted control. That is not that critical as containers running inside pods have restricted execution time, restricted resource requirements and run in a separate namespace.

The implementation of NetworkPolicy restriction is not ready - ideally there should be made an API call to Kubernetes master to create a new NetworkPolicy that would be applied to the pod created in the proceeding API call (using unique label selectors per pod creation).


Application parameters
----------------------

See the parameters section in the `OpenShift YAML template <https://github.com/fridex/thoth-core/blob/master/openshift/template.yaml>`_.
