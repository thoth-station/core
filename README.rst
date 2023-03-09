Thoth-core
==========

Welcome to the Thoth-core project README file!

  **HIBERNATION NOTICE**: The Project is currently hibernating. If you are interested
  in contributing to is, or if you have urgent issues that need to be fixed, please
  reach out to the Thoth team via `an support issue <https://github.com/thoth-station/support/issues/new/choose>`_.

The main aim for this project is to provide a deployment for Thoth core
components. For more information about Thoth project and its goals see `the
Thoth repository <https://github.com/thoth-station/>`_.

You are invited to join our `developer chat <https://chat.google.com/room/AAAAVjnVXFk>`_

Architectural decisions
-----------------------

We keep track of architectural decisions using lightweight architectural decision records. More information on the
used format is available at https://adr.github.io/madr/. General information about architectural decision records
is available at `https://adr.github.io/ <https://adr.github.io/>`_.

Architectural decisions

* `ADR-0000 <docs/adr/0000-use-markdown-architectural-decision-records.md>`_ - Use Markdown Architectural Decision Records
* `ADR-0001 <docs/adr/0001-use-gpl3-as-license.md>`_ - Use GNU GPL as license
* `ADR-0002 <docs/adr/0002-release-policy.md>`_ - Release Policy
* `ADR-0003 <docs/adr/0003-decommision-qeb-hwt.md>`_ - Decommision Qeb-Hwt Bot
* `ADR-0004 <docs/adr/0004-naming-convention-images.md>`_ - Naming convention for Thoth Predictable Stack Images


Demo Session
------------

Past sessions if you missed one: `Thoth Youtube Channel <https://www.youtube.com/channel/UClUIDuq_hQ6vlzmqM59B2Lw/featured>`_.


Interact with Thoth team
-------------------------

How: `Google chat Thoth Developers <https://chat.google.com/room/AAAAVjnVXFk>`_. Please feel free to open an issue and
ask for an invite!

Of course you can always open issues in Thoth station or start contributing to any project under Thoth station.


Community
---------

This repository also contains a description of all the `Project Thoth SIGs (Special Interest Groups) <community/sig-list.md>`_

We have created a short overview of `how we work <docs/TermsAndConditionsForTheScrum.md>`_ too.

Automated Community Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+---------------------+
| Job           | Status              |
+===============+=====================+
| label sync    | |Label Sync Job|    |
+---------------+---------------------+
| GitHub config | |GitHub Config Job| |
+---------------+---------------------+

.. |Label Sync Job| image:: https://prow.operate-first.cloud/badge.svg?jobs=labels&repo=thoth-station/core
.. |GitHub Config Job| image:: https://prow.operate-first.cloud/badge.svg?jobs=thoth-station-peribolos

See `community/README.md` for information on automated repository maintenance.
