# Thoth Release Notes

## Release 2020.10.27

With this release we have focused on knowledge generation: a) by better connecting the backend components and b) by
broadening the security related indicators.

All backend features feed directly into the quality of [Thoth's services](https://github.com/thoth-station/core/blob/master/doc/ROADMAP.md#thoth-services),
more specifically Kebechet and Thamos.

See [Thoth Application Kustomize manifests](https://github.com/thoth-station/thoth-application/tree/v2020.10.27) for a
definitive list of all the versions used in this release.

### Breaking Changes

None, please [file an issue](https://github.com/thoth-station/core/issues) if you hit any!

### Notes

All our end-user tools (like thamos or glyph) are available as part of the
[Thoth Toolbox container image](https://quay.io/repository/thoth-station/thoth-toolbox?tab=info).

### Investigator v0.7

Thoth's investigator is a Kafka based component that consumes all messages produced by Thoth components and reacts to
them by scheduling Argo Workflows.

It has a monitoring system in places that allow Thoth's DevOps team to observe what is happening within Thoth in
terms of Kafka, OpenShift, and Argo for all the different components.

Depending on the type of message received by Investigator, a workflow is scheduled to increase or update the knowledge
stored by Thoth. As always, the [readme](https://github.com/thoth-station/investigator#welcome-to-thoths-investigator-documentation)
is a great source of detailed information.

`thoth-glyph` for this release:

```
0   correct link (#345)                                       features
1   confluent rework (#344)* use wip: messaging ch...       perfective
2   add kebechet run url (#342)* added kebechet ru...         features
3   :pushpin: automatic update of dependency hypot...         features
4   :pushpin: automatic update of dependency thoth...         features
5   :pushpin: automatic update of dependency thoth...         features
6   add docs for thoth investigator (#330)* add do...         features
7   :pushpin: automatic update of dependency hypot...         features
8   :pushpin: automatic update of dependency thoth...         features
9   remove producer from investigator (#329)* remo...          unknown
10  :pushpin: automatic update of dependency mypy ...         features
11  :pushpin: automatic update of dependency thoth...         features
```

### Security Indicators v0.1

We have [introduced Security Indicators](https://github.com/thoth-station/workflows/issues/26): all package releases
observed by Thoth are augmented with [bandit](https://github.com/PyCQA/bandit) related information. These information
is used during advise generation to add or remove packages from candidate stacks. Security Indicators are taken into
consideration when using the ['security' recommendation type](https://thoth-station.ninja/recommendation-types/)
with `thamos advise`.

### Adviser v0.19

Adviser is [Thoth's recommendation system](https://github.com/thoth-station/adviser#thoth-adviser), depending on the
recommendation type, it takes a set of observations into account when resolving a software stack and generating a
recommendation to the user.

This release features the technical requirements to include Security Indicators into a software stack resolution.

If you would like to interact with Thoth from a user's perspective, check [Thamos](https://github.com/thoth-station/thamos).

### Thoth Toolbox v0.5.4

Adding [thoth-glyph](https://github.com/thoth-station/glyph) to our toolbox container image enables a developer to get
a quick view of what changes in which categories. The Glyph readme is a great source of information, please go ahead
and pull the container image from https://quay.io/repository/thoth-station/thoth-toolbox?tab=info

## Release 2020.10.01

We have done a lot of 'internal' updates and maintenance, focusing on renewing the way Thoth handles learning
about new releases of packages.

See [Thoth Application Kustomize manifests](https://github.com/thoth-station/thoth-application/tree/v2020.10.01) for a
definitive list of all the versions used in this release.

### Investigator v0.5

[Thoth Investigator](https://github.com/thoth-station/investigator/) is an agent sent out by Thoth to seek new
information on packages, that will yield observations and knowledge to Thoth.

It is called by Thoth components to gather new messages after investigations about possible observations on packages.

Thoth Investigator centre of investigation receives those messages and after further investigation decides what
actions need to be taken depending on the messages received, so that Thoth can increase its knowledge.

This release of investigator is migrating more components of [Thoth to a Kafka-based messaging](https://github.com/thoth-station/messaging).
In addition to that, we re-schedule adviser's Argo Workflows that have not created results before. The re-scheduled
workflow will create more meaningful advise as Thoth might have learned about packages being used (which might have
been unknown on the first run) and help Thoth keeping its knowledge up to date.

### Thoth Service Level Objective (SLO) reporter v0.7

[Thoth's Service Level Objectiv (SLO) Reporter](https://github.com/thoth-station/slo-reporter) purpose is to share
Thoth's achievements and behaviour with the outside world.

We have extended it's README and developers guide, so that understand it's concepts and components get easier. A lot
of Thoth internal observability has been added to a large set of components, all metrics are surfacing via SLO reporter
into Grafana dashboards.

### Breaking Changes

None are known, please [file issues](https://github.com/thoth-station/core/issues) if you hit any!

### Notes

These enhancements have been deployed and are available to [Qeb-Hwt](https://github.com/apps/Qeb-Hwt) immediately.

## Release 2020.09.17

First of all, why do we use [CalVer](https://calver.org/) for the core repository? Because the Thoth Services and
Tools consist of a large set of [GitHub-hosted repositories](https://github.com/thoth-station/),
[Python modules](https://pypi.org/search/?q=thoth-), [container images](https://quay.io/organization/thoth-station) and
even [RPMs](https://pkgs.org/search/?q=micropipenv).
Any of these components might yield to a release at any time. This release note file covers the aggregation of important
releases in the contexts of

* Thoth Service - our back end services, the knowledge generation
* the toolbox - command line tools and their packages

### Index of Justifications

Starting with this release, we publish a [human-readable list of justifications](https://thoth-station.ninja/justifications). This list is referenced from any `thamos advise` output on the terminal, or any pipeline integration. Its purpose is
to show the knowledge contained in Thoth's services and to act as a jump-page to more detailed and background information.
Especially the jump-page character is important to users, as we don't want to clutter the terminal/pipeline output, but
want to reveal to results of our reinforcement learning process in a transparent way.

### Breaking Changes

None are known, please [file issues](https://github.com/thoth-station/core/issues) if you hit any!

### Adviser

[Adviser](https://github.com/thoth-station/adviser) is Thoth's recommendation engine and software stack generator.

* [a review of CPU types, and the way we create recommendation for AVX2 and Tensorflow has been done](https://github.com/thoth-station/adviser/issues/1022)
* [some new TensorFlow related observations/justfications have been created](https://github.com/thoth-station/adviser/commit/46da6d0fa8208a36f6804049b600c5e7e0ae83ea)
* [a recommendation to configure MKL correctly was added](https://github.com/thoth-station/adviser/commit/c7474f7720773a6acc79321eb4d8d73aa671df3f)
* general stabilization of Argo-Workflows based backend services
* adviser now supports advises specific for manifest changes (e.g. adjusting environment variables of OpenShift
DeploymentConfigs)

### Notes

These enhancements have been deployed and are available to [Qeb-Hwt](https://github.com/apps/Qeb-Hwt) immediately.
