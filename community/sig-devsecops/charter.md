# SIG DevSecOps Charter

This charter adheres to the conventions described in the [Kubernetes Charter README] and uses the Roles and Organization Management outlined in [sig-governance]. For all things taken from the Kubernetes community, we use scaled down variants, Kubernetes documents are references.

## Scope

This SIG covers all the tools and supporting container images that deliver Thoth-Station
applications, as well as the build pipelines and Continuous Integration systems
that enable the automated builds.

This includes the discussion related to the release process of the Thoth-Station
applications, the build pipelines themselves, supporting container images, tooling,
and architectural decisions.

### In scope

- Pipelines to build and publish application container images
- Supporting container images
- End-user oriented content about Thoth pipelines and supporting images
- GitOps configurations to deploy the services
- Release management for Thoth-Station

### Out of scope

- Operation of the clusters that host the services

## Roles and Organization Management

This sig follows adheres to the Roles and Organization Management outlined in [sig-governance].

### Subproject Creation

SIG Chairs can create subprojects without requiring member votes.

[kubernetes charter readme]: https://github.com/kubernetes/community/blob/master/committee-steering/governance/README.md
[sig-governance]: https://github.com/kubernetes/community/blob/master/committee-steering/governance/sig-governance.md
[sig-subprojects]: https://github.com/kubernetes/community/blob/master/sig-YOURSIG/README.md#subprojects
