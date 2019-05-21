TEP: 3
Title: Organizing Service Configuration and Secrets
Author: Christoph Görn <goern@redhat.com>
Status: Active
Type: Architecture
Content-Type: text/x-rst
Created: 2018-Nov-06

Organizing Service Configuration and Secrets
============================================

Having multiple services requires a consistent configuration of shared resources, for example Ceph storage or the 
Graph Database. At the same time services should not depend on the same configuration item, eg DEBUG set once and
for all services.

ConfigMaps
----------

Secrets
-------

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
