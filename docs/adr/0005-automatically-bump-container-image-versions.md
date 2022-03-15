# Automatically bump the version of base images used to generate container images

* Status: proposed
* Date: 2022-02-15

Technical Story: As a maintainer of Thoth, I would like to automatically update the version of the base images used to generate new container images of some components (see: https://github.com/thoth-station/kebechet/issues/991)

## Context and Problem Statement

When new base image versions used to genereate container images for Thoth components are released on Quay, it would be practical to update them automatically instead of manually opening `Bump <component name> to vx.y.z in <environment>` pull requests in the concerned repositories (Example: https://github.com/thoth-station/thoth-application/pull/2314).

## Considered Options

* Implement a simple Python script to bump the base image versions used to deliver container images in `.aicoe-ci.yaml`, `.thoth.yaml` or similar files for eventual uses outside of the project.
    * 1) Integrate this script in the AICoE-CI pipeline logic
    * 2) Integrate this script in Kebechet

## Decision Outcome

Chosen option: 1). For the moment, this script has been integrated in the AICoE-CI pipeline logic, but it could eventually be reused in Kebechet if needed.

### Positive Consequences <!-- optional -->

* Keeping the base image versions we use up-to-date for active repositories.
* Base image version updates are made automatically, which is less error-prone and time-consuming for developers compared to making the update manually.

## Links <!-- optional -->

* Current action items and building blocks proposal: https://github.com/thoth-station/kebechet/issues/991#issuecomment-1039220686
* Script implementation in `pipeline-helpers`: https://github.com/thoth-station/pipeline-helpers/pull/45
* Script integration in the `aicoe-ci` pipeline logic: https://github.com/AICoE/aicoe-ci/pull/170
* Demo: https://www.youtube.com/watch?v=Uwc7WS4SnL4&t=2s&ab_channel=ThothStation
<!-- markdownlint-disable-file MD013 -->
