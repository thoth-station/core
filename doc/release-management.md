# Release Management

## Integration new source code

New source code is integrated via GitHub Pull Requests:

1. each new feature should come from a feature branch
2. each fix should come from a issue branch
3. general editions should come from the master branch

Each Pull Request is build and tested by a CI system. CI will write back status updates to the Pull Request.

A Pull Request may carry the 'work-in-progress' or 'do-not-merge' label, this forbids merging. A Pull Request may carry the 'needs-rebase' label, it will not be merged.

If the most current CI status of context 'continuous-integration/jenkins/pr-merge' is not 'success' the 'approved' label will be removed from the RP.

A Pull Request carrying the 'approved' label will be merged.