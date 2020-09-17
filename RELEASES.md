# Release 2020.09.17

This of all, why do we use [CalVer](https://calver.org/) for the core repository? Because the Thoth Services and
Tools consist of a large set of [GitHub-hosted repositories](https://github.com/thoth-station/),
[Python modules](https://pypi.org/search/?q=thoth-), [container images](https://quay.io/organization/thoth-station) and
even [RPMs](https://pkgs.org/search/?q=micropipenv).
Any of these components might yield to a release at any time. This release note file covers the aggregation of important
releases in the contexts of

* Thoth Service - our back end services, the knowledge generation
* the toolbox - command line tools and their packages

## Index of Justifications

Starting with this release, we publish a [human-readable list of justifications](https://thoth-station.ninja/justifications). This list is referenced from any `thamos advise` output on the terminal, or any pipeline integration. Its purpose is
to show the knowledge contained in Thoth's services and to act as a jump-page to more detailed and background information.
Especially the jump-page character is important to users, as we don't want to clutter the terminal/pipeline output, but
want to reveal to results of our reinforcement learning process in a transparent way.

## Breaking Changes

None are known, please [file issues](https://github.com/thoth-station/core/issues) if you hit any!

## Adviser

[Adviser](https://github.com/thoth-station/adviser) is Thoth's recommendation engine and software stack generator.

* [a review of CPU types, and the way we create recommendation for AVX2 and Tensorflow has been done](https://github.com/thoth-station/adviser/issues/1022)
* [some new TensorFlow related observations/justfications have been created](https://github.com/thoth-station/adviser/commit/46da6d0fa8208a36f6804049b600c5e7e0ae83ea)
* [a recommendation to configure MKL correctly was added](https://github.com/thoth-station/adviser/commit/c7474f7720773a6acc79321eb4d8d73aa671df3f)
* general stabilization of Argo-Workflows based backend services
* adviser now supports advises specific for manifest changes (e.g. adjusting environment variables of OpenShift
DeploymentConfigs)

## Notes

These enhancements have been deployed and are available to [Qeb-Hwt](https://github.com/apps/Qeb-Hwt) immediately.
