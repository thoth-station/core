Thoth-core
==========

Welcome to the Thoth-core project README file!

The main aim for this project is to provide a deployment for Thoth core
components. For more information about Thoth project and its goals see `the
Thoth repository <https://github.com/thoth-station/thoth>`_.

Installation
------------

The Ansible playbooks require a few Roles to be unstalled, and a vault password.

.. code-block:: console

 git clone https://github.com/thoth-station/core
 cd core
 ansible-galaxy install --role-file=requirements.yaml --roles-path=/etc/ansible/roles --force # to update any existing role
 vim playbooks/group_vas/all/vars  # review deployment parameters
 ansible-playbook playbooks/provision.yaml

Deprovisioning
--------------

.. code-block:: console

  oc login <OCP_URL>
  cd core
  ansible-playbook playbooks/deprovision.yaml --extra-vars THOTH_NAMESPACE=<NAMESPACE>

See `operations documentation
<https://github.com/thoth-station/core/blob/master/doc/operations.rst>`_ for
more info.

Documentation
-------------

Documentation on Thoth's architecture `can be found here
<https://thoth-station.ninja/docs/developers/adviser/>`_.

