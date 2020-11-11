# GitOps repository url should be part of `.thoth.yaml`

* Status: proposed
* Date: 2020-Nov-11

Technical Story: As a Reproducible Deployment Pipeline, I want to take thamos advises from the build process, so that
I can apply recommendations within the deployment process.

## Context and Problem Statement

[Describe the context and problem statement, e.g., in free form using two to three sentences. You may want to articulate the problem in form of a question.]

Looking at the [Reproducible Deployment Pipeline](https://github.com/thoth-station/core/blob/master/docs/ROADMAP.md#reproducible-deployment-pipeline)
we need to reconfigure deployment configurations based on the software stack advises, eg intel-tensorflow uses MKL, therefore we
need to set certain environment variables. Advises on the software stack will be used/processed during the build process,
advises on the deploment configuration during deployment process, both are decoupled. To enable the information transfer,
one task of the build pipeline could open a pull request to change the deployment configuration, therefore it needs to
know where the GitOps repository is located.

## Decision Drivers

* respect GitOps practice, at the same time support Cyborg practice
* Tekton is our pipeline driver/controller, ArgoCD is a sub-component

## Considered Options

* GitOps repository url is not part of `.thoth.yaml`, write out the advise so that it can be stored within the build container image, this information can be used by the
deployment pipeline to change configuration during deployment. how?
* GitOps repository url is part of `.thoth.yaml`, it can be used by said part of a build pipeline
* DeploymentConfig file is part of the application source code repository, and can be modified by s2i-thoth

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

* [Link type] [Link to ADR] <!-- example: Refined by [ADR-0005](0005-example.md) -->
* … <!-- numbers of links can vary -->

<!-- markdownlint-disable-file MD013 -->