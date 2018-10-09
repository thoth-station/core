Thoth-core
==========

Welcome to the Thoth-core project README file!

The main aim for this project is to provide a deployment for Thoth core
components. For more information about Thoth project and its goals see `the
Thoth repository <https://github.com/thoth-station/thoth>`_.

Installation
------------

The Ansible playbooks require a few Roles to be unstalled.

.. code-block:: console

 git clone https://github.com/thoth-station/core
 cd core
 ansible-galaxy install -r requirements.yaml
 vim playbooks/provision.yaml  # review deployment parameters
 ansible-playbook playbooks/provision.yaml

Deprovisioning
--------------

.. code-block:: console

  oc login <OCP_URL>
  cd core
  ansible-playbook playbooks/deprovision.yaml --extra-vars THOTH_NAMESPACE=<NAMESPACE>

See `operations documentation <https://github.com/thoth-station/core/blob/master/doc/operations.md>`_ for more info.

Architecture Overview
---------------------

The whole deployment is divided into three namespaces (or two OpenShift projects) - ``thoth-frontend``, ``thoth-middletier`` and
``thoth-backend``.

.. figure:: https://raw.githubusercontent.com/thoth-station/core/master/images/design.png

Frontend Namespace
##################

The ``thoth-frontend`` is used as a management namespace. Services running in this namespace have usually
assigned a service account for running and managing pods that are available
inside the ``thoth-middletier`` and ``thoth-backend`` namespaces.


A user can interact with the user-facing API that is the key interaction
point for a user or bots. `The user-facing API
<https://github.com/thoth-station/user-api>`_ specifies its endpoints using
Swagger/OpenAPI specification. See `Thamos repo for a library/CLI for
interacting <https://github.com/thoth-station/thamos>`_ (and its
documentation) with the user API service and `the user API service repo
<https://github.com/thoth-station/user-api>`_ itself for more info.

Besides user API there are run periodically CronJobs that keep application in
sync and operational:

* `cleanup-job <https://github.com/thoth-station/cleanup-job>`_ - a job responsible for cleaning up resources left in the cluster
* `graph-refresh-job <https://github.com/thoth-station/graph-refresh-job>`_ - - a job responsible for scheduling analyses of packages that were not yet analyzed
* `graph-sync-job <https://github.com/thoth-station/graph-sync-job>`_ - a job responsible for syncing data in JSON format persisten on Ceph to JanusGraph database
* `package-releases-job <https://github.com/thoth-station/package-releases-job>`_ - a job responsible for tracking new releases on Python's package index (the public one is `PyPI.org <https://pypi.org>`_)
* `cve-update-job <https://github.com/thoth-station/cve-update-job>`_ - a job responsible for gathering CVE information about packages

Middletier Namespace
####################

The middletier namespace is used for analyzes and actual resource consuming
tasks that compute results for Thoth's database. This namespace was separated
from the frontend namespace to guarantee application
responsibility. All pods that requiure compute results for the database are
scheduled in this namespace. This namespace has an allocated pool of
resources for such un-predicable amount of computational pods needed for this
purpose (so pods are not scheduled besides running user API possibly making
user API non-responsive).

As some of the analyses performed can execute possibly malicious code, this
namespace is guarded using network policy rules to run containers in fully
isolated environment (besides namespace separation). A special service -
`result API <https://github.com/thoth-station/result-api>`_ abstracts away
any database operations (that can be possibly dangerous when executing an
untrusted code). Each analyzer that is run in this namespace seriales its
results to a structured (text) JSON format and these results are submited to
the user API service that stores results in the Ceph object storage. All
results computed by Thoth are first stored in JSON format for later analyses
and making the graph instance fully recovarable and reconfigurable based on
previous results.

Currently, there are run following analyzers in the middletier namespace:

* `package-extract <https://github.com/thoth-station/package-extract>`_ - an analyzer responsible for extracting packages from runtime/buildtime environments (container images)
* `solver <https://github.com/thoth-station/solver>`_ - an analyzer run to gather information about dependencies between packages (on which packages the given package depends on?, what versions satisfy version ranges?) and gathers observations such as whether the given package is installable into the given environment and if it is present on a Python package index
* `dependency-monkey <https://github.com/thoth-station/dependency-monkey>`_ - an analyzer that dynamically constructs package stacks and submits them to `Amun <https://github.com/thoth-station/amun-api>`_ for dynamic analysis (can be the given stack installed?, what are runtime observations - e.g. performance index?) (this is currently WIP)

Backend Namespace
#################

The backend part of application is used for executing code that, based on
gathered information from analyzers run in the middletier namespace, compute
results for actual Thoth users (bots or humans).

This namespace is, as in the case of middletier namespace, allocated pool of
resources that serve in this case user requests. Each time a user requests a
recommendation to be computed, pods are dynamically created in this namespace
to compute results for users.

As of now, there are run the folowing analyzers to compute recommendations
for a user:

* `adviser <https://github.com/thoth-station/adviser>`_ - a recommendation engine computing stack level recommendations for a user for the given runtime environment
* `provenance-checker <https://github.com/thoth-station/adviser>`_ - an analyzer that checks for provenance (origin) of packages so that a user uses correct packages from corrent package sources (Python indexes) - note that Python packaging format does not guarantee this - neigher Pipenv nor pip itself! (the implementation now lies besides adviser)

Cluster requirements
--------------------

In order to create NetworkPolicy objects, there needs to be enabled the ``ovs-networkpolicy`` plugin - see `docs for more details <https://docs.openshift.com/container-platform/3.6/admin_guide/managing_networking.html#admin-guide-networking-networkpolicy>`_ and OpenShift 3.5 or newer as NetworkPolicy objects were introduced starting `OpenShift version 3.5 as a tech preview <https://blog.openshift.com/whats-new-in-openshift-3-5-network-policy-tech-preview/>`_.

As of now, NetworkPolicy is not applied so there are no network restrictions to created pods. This enables pods to reach outside world without any fine-granted control. That is not that critical as containers running inside pods have restricted execution time, restricted resource requirements and run in a separate namespace.

The implementation of NetworkPolicy restriction is not ready - ideally there should be made an API call to Kubernetes master to create a new NetworkPolicy that would be applied to the pod created in the proceeding API call (using unique label selectors per pod creation).
