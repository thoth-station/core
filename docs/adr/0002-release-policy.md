# Project Thoth Release Policy

* Status: proposed
* Date: 2020-Nov-04

Technical Story: As an Open Source project, we want to document the policies and guideline on how we create a new
release.

## Context and Problem Statement

Project Thoth itself consists of many components all having their own release cycles and delivery artifacts such as
container image or Python libraries.

## Considered Options

* a monolithic, coordinated release of all components by creating a tag within the thoth-application repository
* have a rolling release, and no tags on any repository

## Decision Outcome

Chosen option: we do a monolithic, coordinated release, because it will enable us to have a release at the
project/product level while maintianing freedom of others to update.

### Positive Consequences <!-- optional -->

* users have a clear base line of versions, these versions have been tested with each other and have
  undergone integration testing.
* a release can be referenced from documents, so that operational procedures have a clear relationship with component
  versions being used
* we can maintain sets of different versions for different deployment environments
* we can provide a version string with each API provided by the project

### Negative Consequences <!-- optional -->

* A release might not contain the latest versions of components

<!-- markdownlint-disable-file MD013 -->
