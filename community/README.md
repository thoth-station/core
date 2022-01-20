## Repository configuration

The [github-config.yaml](./github-config.yaml) file contains the details of the
GitHub configuration for our organization.

This file is used by
[Peribolos](https://github.com/kubernetes/test-infra/tree/master/prow/cmd/peribolos)
to apply the configuration to the various repositories. Check the Peribolos
documentation for more details.

## Updating SIG information

Information about SIGs is sourced from the [sigs.yaml](./sigs.yaml) file.

To generate all the SIG documentation and update the OWNERS files from the
source file, use the `generate` or `generate-dockerized` targets in the
[Makefile](./Makefile), e.g.:

```
make
```

(`genenerate` is the default target).

This uses the [generator app](https://github.com/kubernetes/community/tree/master/generator) from the
Kubernetes community.

## Updating labels.md

The [labels.md](./labels.md) file that documents the available labels is
generated from the source [labels.yaml](./labels.yaml) file that is used by prow to
maintain the labels on the repos.

To update the document after a change in the source, use the [label_sync](https://github.com/kubernetes/test-infra/tree/master/label_sync) application
with the `docs` action. An containerized version invocation is included in the [Makefile](./Makefile):

```
make generate-dockerized
```
