# Thoth GitHub Action ADR

* Status: proposed
* Date: 2022-May-16

Technical Story: we would like to create a new Thoth integration via a GitHub Acttion to advise users on the dependencies used in their repositories.

## Context and Problem Statement

The Thoth GitHub Action was originally supposed to be implemented to advise on the dependencies present in the [Packit repository](https://github.com/packit/packit), but should be extendable to other repositories as well with different requirement formats (`pip`, `pipenv`...).

The primary goal of this Action would be to advise on the **security** aspects of dependencies of a project by providing a mean to:

* Identify CVE present in the versions of the packages used in the project, so that users can eventually block Pull Requests introducing vulnerable dependencies
    * Comment on the Pull Requests with a list of CVE found for the current package versions
    * Log all stack info in the action workflow
    * Provide a link to Thoth Search UI to browse the advise results
    * Fail the workflow to eventually block the Pull Request
* Get security insights on the dependency stack introduced by a Pull Request by returning the content of the stack info (Security Scorecards data, warnings, info, etc)
    * Log stack info in the action workflow
    * Provide a link to Thoth Search UI to browse the advise results
* Score the current dependency stack and allow repository maintainers to display this score as a badge in the landing page of their repository as an indicator of application dependencies health
    * Get the software stack score provided in the advise result and normalize it if needed
    * Create a [status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) for the workflow running the Thoth GitHub Action indicating the score of the software stack on the merge of a Pull Request modifying the requirements file.

## Considered Options

### Setting up the Action on a repository

```
name: User CI workflow
on:
  push:
    paths:
      - 'requirements.txt'
      - 'Pipfile'
jobs:
  validate-dependencies:
    runs-on: ubuntu-latest
    name: Get Thoth recommenations on your dependencies
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Get Thoth security advisories
        id: thoth-advise
        uses: thoth-station/thoth-github-action@v1
        with:
          path: './requirements.txt'
```

The Thoth GitHub Action requires prior actions already available on the GitHub Marketplace to work on a repository Pull Request workflow, such as [`actions/checkout`](https://github.com/actions/checkout) to checkout the current repository or [`actions/setup-python`](https://github.com/actions/setup-python) to set up a Python environment where the Python parts of the Action can be run:

```
steps:
  - uses: actions/checkout@v3
  - uses: actions/setup-python@v2
    with:
      python-version: 3.8

```

To trigger the workflow only when necessary, it can be configured to trigger the Action on a `push` event which modifies the dependency requirements file of the project (`Pipfile`, `requirements.txt`, etc):

```
on:
  push:
    paths:
      - 'requirements.txt'
      - 'Pipfile'
```

### Thoth GitHub Action architecture

![Thoth GitHub Action diagram](./images/Thoth-GitHub-Action-ADR.drawio.png, "Thoth GitHub Action architecture diagram using Thamos CLI to generate advise")

Possible alternatives would be to:

* Make a call directly to the User API via a bash script to avoid issues linked to the creation of a `.thoth.yaml` configuration file and to use a Python script to process the advise result only
* Use Thamos as a library to get the advise result

However, those options would not be as easily maintainable.

## Decision Outcome

To be done.
