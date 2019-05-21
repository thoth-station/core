TEP: 2
Title: Thoth Software Architecural Principals
Author: Christoph Görn <goern@redhat.com>
Status: Active
Type: Architecture
Content-Type: text/x-rst
Created: 2018-Nov-05

Thoth Software Architecural Principals
======================================

Moving Thoth forward, from a proof of concept phase to a more mature software project, the need to document general
architecural and design principals grows. This document captures the current thinking on this topic.

Software Components
-------------------

Microservices
-------------

Application Programming Interfaces
----------------------------------

OpenShift Applications
----------------------

Some of Thoth's componets are grouped as OpenShift applications, eg all the components belonging to one application
carry the `app` label and the `component` label.

The `app` label determines the application. Currently the following applications are use:

 
| all label   | Application Name         | Description                                      |
|------------:|--------------------------|--------------------------------------------------|
| website     | Thoth internal Website   | an internal website containing some useful links |
| thoth       | Thoth Core               | core services and jobs                           |
| amun        | Amun                     | all Amun services and jobs                       |
| sesheta     | Cyborg Team member       | used for integration with GitHub, Zuul           |
| kebechet    | Cyborg Team member       | Junior Developer helping all of us!              |
| zuul        | Cyborg Team member       | base images for Zuul jobs                        |

OpenShift Operator Pattern
--------------------------


Copyright
=========

Copyright (C) 2018 Red Hat Inc.

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the file named "fdl-1.3.txt".



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
