PEP: 1
Title: Workload management in Thoth
Author: Christoph Görn <goern@redhat.com>
Status: Draft
Type: Solution Design
Content-Type: text/x-rst
Created: 2018-Oct-26


Abstract
========

This TEP defines requirements, includes considerations and proposeds
a workload management solution for Thoth's Graph Sync, and Graph Refresh
tasks.

Rationale
=========

Implementing a trivial (or brute force) cronjob based graph sync or 
graph refresh does not scale. We need to continuously add and update 
information in the graph database. 

Requirements
============

All app/update tasks should happen asynchruounesly. Solver or Analysis
documents stored on disk should be processed individually to split up 
huge chunks of work into small chuncks.

Proposal
========

Periodic Job
------------

Periodic jobs should scan for new solver or analysis documents stored on disk. 
The periodic job should defere add/update operations to a worker, this worker 
should read the document and add/update the graph database. Deferral of operations
should be processed via a workload manager.

Worker
------

The worker should read the solver or analysis file, parse its content and add/update
information in the graph database. The worker should process one document.

Workload Manager
----------------

The workload manager should be able to execute workers based on rules. Using this 
feature the workload manager should be able to dynamically adopt the number of 
workers executed at the same time.

Solution Alternatives
=====================

OpenShift Operator
------------------

Jobs, Workers, and the Workload manager could be implemented using the Operator
pattern [1]_.

Resources
=========
n/a

References
==========
.. [1] `Introducing the Operator Framework: Building Apps on Kubernetes` https://blog.openshift.com/introducing-the-operator-framework/

Copyright
=========

Copyright (C) 2018 Christoph Görn

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
