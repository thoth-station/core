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
information in the graph database. All app/update tasks should happen
asynchruounesly. Solver or Analysis documents stored on disk should 
be processed individually to split up huge chunks of work into small 
chuncks.

Resources
=========


References
==========


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