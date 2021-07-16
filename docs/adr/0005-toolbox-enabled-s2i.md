# Enable S2I containers to be used with `toolbox`

* Status: proposed
* Date: 2021-Jul-16

Technical Story: As a Data Scientist, I want to use `toolbox enter` with any ODH/PS container image, so that I can run my NLP-PyTorch Jupyter Notebbok, and so that I can use horus to manage my notebook's dependencies.

## Context and Problem Statement

We want Data Scientists to be able to start working on Jupyter notebooks on their local laptops, and later on easily
migrate their work to Open Data Hub. Therefor we wan to provide the same container images and tools. If they are working
on their local machines, the integration with the local operating system shall be as thighly as possible, therefor we
want them to use `toolbox`.

## Decision Drivers

* enhance user experience

## Considered Options

* 'toolbox layer ontop S2I' standard name currently, but not everyone knows what S2I is.
* add toolbox requirments to `s2i-minimal-notebook`

## Decision Outcome

### Positive Consequences

### Negative Consequences

## Pros and Cons of the Options

### Layer Toolbox ontop of S2I images

* Good, because it keeps the amount of packages in very basic/low-level images small
* Bad, because we need an overlay and pipelinerun for every image we create

### Toolbox as part of `s2i-minimal-notebook`

* Good, because it enables all notebooks to be used by `toolbox`
* Bad, it addes dependencies not required for ODH usage

<!-- markdownlint-disable-file MD013 -->
