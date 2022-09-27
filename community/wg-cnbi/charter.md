# WG Custom Notebook Image (CNBi) Charter

The goal of this working group (WG) is to design and implement an MVP for the backend side of the Custom Notebook Image (CNBi) functionality of Open Data Hub (ODH).

The WG is a continuation of the work of the [BYON WG](https://github.com/open-services-group/community/blob/main/wg-byon-build-pipelines/README.md). The work produced by the working group aims at meeting the requirements specified in the RHODS epics about the functionality, including:

- Bring Your Own Notebook (BYON) (phase 1): [Custom notebooks - phase 1](https://issues.redhat.com/browse/RHODS-2211)
- CNBi (phase 2): [Custom notebooks - phase 2](https://issues.redhat.com/browse/RHODS-3203)

For reference, deliverables for phase 1 (BYON) were tracked in the [byon repository](https://github.com/open-services-group/byon/) and its corresponding [project planning board](https://github.com/orgs/open-services-group/projects/3).

## Scope

The focus of this WG is on the backend components that handle the creation, validation, and importing of container images for use into ODH, as well as the software stack guidance service provided to the users of these images.

### In scope

- The CNBi operator
- Tekton Pipeline definitions that implement the CNBi / BYON functionality
- Thoth APIs that contribute to the requirements of the CNBi functionality on ODH
- Coordination with ODH in integrating the funtcionality
- Deployment of the PoC and coordination with Operate First and OS-Climate on its usage

### Out of scope

- ODH User Interface design and implementation

## Stakeholders

- Thoth SIGs:
  - DevSecOps
  - Stack Guidance
  - User Experience
- ODH SIGs:
  - ML-DevExp
  - Platform

## Deliverables

- Documentation of the design of the backend, the components involved, the interactions between them, and the interface between ODH and the backend.
  - Documentation will be stored in the https://github.com/thoth-station/opendatahub-cnbi/ repository.
- An evolution of the [meteor operator](https://github.com/thoth-station/meteor-operator) that acts as the main controller for the CNBi functionality.
- A set of Tekton / OpenShift pipelines definitions that implement the functionality.
- A working PoC of the operator and pipelines, with ODH integration when available, ready to use by a target group: the OS-Climate project.

## Disband criteria

If stakeholder SIGs and the WG decide all features described in the `In Scope` section are complete and no more discussions and investigations are needed in this WG, they may decide to disband this WG.
