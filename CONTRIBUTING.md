# Contributing Guidelines

Thanks for your interest in contributing to `Thoth Station`.

## Reporting Bugs

Before creating bug reports, please check a [list of known issues](https://github.com/issues?q=is%3Aopen+is%3Aissue+archived%3Afalse+user%3Athoth-station+sort%3Acreated-asc) to see
if the problem has already been reported (or fixed in a main branch).

**Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.
You can also comment on the closed issue to indicate that upstream should provide a new release with a fix.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues.
When you are creating an enhancement issue, **use a clear and descriptive title** and **provide a clear description of the suggested enhancement** in as many details as possible.

## Guidelines for Developers

If you would like to contribute code to the `Thoth` project, this section is for you!

### Is this your first contribution?

Please take a few minutes to read GitHub's guide on [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).
It's a quick read, and it's a great way to introduce yourself to how things work behind the scenes in open-source projects.

### Dependencies

If you are introducing a new dependency, please make sure it's added to:

- `Pipfile`
- `setup.py` if its a package

### Documentation

If you want to update documentation, [README.md](README.md) is the file you're looking for.

### How to contribute code to Project Thoth

1. Create a fork of a repository.
2. Create a new branch just for the bug/feature you are working on.
3. Once you have completed your work, create a Pull Request, ensuring that it meets the requirements listed below.

### Requirements for Pull Requests (PR)

- Use `pre-commit` (see [below](#checkerslintersformatters--pre-commit)), a positive status in context `aicoe-ci/prow/pre-commit` is required for merging
- All tests have to pass, a positive status in context `aicoe-ci/prow/pytest` might be required for merging
- Cover new code with a test case (new or existing one).
- Use common sense when creating commits, not too big, not too small. You can also squash them at the end of review. See [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/).
- Rebase against updated `main` branch before creating a PR to have linear git history.
- Create a PR against the `main` branch.

### Checkers/linters/formatters & pre-commit

To make sure our code is [PEP8](https://www.python.org/dev/peps/pep-0008/) compliant, we use:

- [black code formatter](https://github.com/psf/black)
- [Flake8 code linter](http://flake8.pycqa.org)
- [mypy static type checker](http://mypy-lang.org)

There's a [pre-commit](https://pre-commit.com) config file in [.pre-commit-config.yaml](.pre-commit-config.yaml).
To [utilize pre-commit](https://pre-commit.com/#usage), install pre-commit with `pip3 install pre-commit` and then either:

- `pre-commit install` - to install pre-commit into your [git hooks](https://githooks.com). pre-commit will from now on run all the checkers/linters/formatters on every commit. If you later want to commit without running it, just run `git commit` with `-n/--no-verify`.
- Or if you want to manually run all the checkers/linters/formatters, run `pre-commit run --all-files`.

Thank you for your interest!
