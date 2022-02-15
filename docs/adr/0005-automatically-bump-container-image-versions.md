# Automatically bump the version of base images used to generate container images

* Status: proposed
* Date: 2022-02-15

Technical Story: As a maintainer of Thoth, I would like to automatically update the version of the base images used to generate new container images of some components (see: https://github.com/thoth-station/kebechet/issues/991)

## Context and Problem Statement

When new base image versions used to genereate container images for Thoth components are released on Quay, it would be practical to update them automatically instead of manually opening `Bump <component name> to vx.y.z in <environment>` pull requests in the concerned repositories (Example: https://github.com/thoth-station/thoth-application/pull/2314).

## Considered Options

* Implement a simple Python script to bump the base image versions used to deliver container images in `.aicoe-ci.yaml`, `.thoth.yaml` or similar files for eventual uses outside of the project.
    * Integrate this script in the AICoE-CI pipeline logic
    * Integrate this script in Kebechet
    
## Decision Outcome

Chosen option: "[option 1]", because [justification. e.g., only option, which meets k.o. criterion decision driver | which resolves force force | … | comes out best (see below)].

### Positive Consequences <!-- optional -->

* [e.g., improvement of quality attribute satisfaction, follow-up decisions required, …]
* …

### Negative Consequences <!-- optional -->

* [e.g., compromising quality attribute, follow-up decisions required, …]
* …

## Pros and Cons of the Options <!-- optional -->

### [option 1]

[example | description | pointer to more information | …] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* … <!-- numbers of pros and cons can vary -->

### [option 2]

[example | description | pointer to more information | …] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* … <!-- numbers of pros and cons can vary -->

### [option 3]

[example | description | pointer to more information | …] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* … <!-- numbers of pros and cons can vary -->

## Links <!-- optional -->

* Current action items and building blocks proposal: https://github.com/thoth-station/kebechet/issues/991#issuecomment-1039220686

<!-- markdownlint-disable-file MD013 -->
