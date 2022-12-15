# Support Policy

This document outlines the support policy for Project Thoth. For general information how and where to contact us,
please see our [help page](https://thoth-station.ninja/help/).

## Supported Runtime Environments

When adding new content to Thoth's Knoweldge Graph, we follow (roughly) the following policy:

1. what runtime is used by RHODS/Open Data Hub? Right now most data science work is based on ubi8-py38
2. what runtime is the latest release and maintained by Red Hat? ubi9-py39
3. based on our research (py311 due to perf incr.), see also https://www.phoronix.com/review/python-311-performance

## End of Life

We will disable solvers and the corresponding Python versions when they reach end of life. The data aggregated by
Project Thoth will be kept in the Knowledge Graph for as long as possible. We will not delete data from the
Ceph storage, but might disable its use for advises.
