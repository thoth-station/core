Git Hooks Management
====================

Overview
--------

**Git Hooks**: A trigger to automate the checks before operations like
commit, push and etc.

Our Git hooks are designed to check for proper formatting, linting, and
test checking for no-pull-request-breakage. Using these Git hooks would
ease the development and would be a good practice.

Once the git hooks are set up in the clone repository/repositories in
your local.

***Functionality of pre-commit***: Whenever you try to ``git commit``
the pre-commit hook will execute to process before committing. Your
commit will be committed but you will be able to notice the warning for
the formatting, and linting flaws in your commit.

**NOTE**: To by-pass the pre-commit test, use either of the commands: \*
``THOTH_NO_PRECOMMIT_TEST=1 git commit -m "<commit msg>"`` \*
``git commit -m "<commit msg>" --no-verify"``

***Functionality of pre-push***: Whenever you try to ``git push`` the
pre-push hook will execute to process before pushing. Your push request
will be executed but you will be able to notice the warning for the test
passing flaws in your commit.

**NOTE**: To by-pass the pre-commit test, use either of the commands: \*
``THOTH_NO_PREPUSH_TEST=1 git push origin master`` \*
``git push origin master --no-verify"``

Install Git hooks on local
--------------------------

Our Git hooks are stored under the directory *.git_init/hooks*.

Once cloning the repository is completed, run the following command from
the cloned repository to initiate the Git hooks:

``git init --template .git_init``

This command will activate the Git hooks from our *.git_init* directory,
by adding the hooks in *.git_init* to *.git/hooks*.

Creating new hooks
------------------

Create a hook script in any preferred language BASH, PERL, and PYTHON.
It should be executable.

**NOTE**: Naming convention of the hook script is pre-defined based upon
the functionality method they serve. Please only name the hook scripts
appropriately and same as one of the example scripts in the *.git/hooks*
or else SCRIPT WON’T BE EXECUTED.

**ENABLING the hook script**:

1. **For self usage**:To enable a hook script, place the file in the
   ‘*hooks*’ subdirectory of your *.git* directory that is named
   appropriately (without any extension) and is executable.
2. **For organization usage**: To enable a hook script, place the file
   in the ‘*hooks*’ subdirectory of our *.git_init* directory that is
   named appropriately (without any extension) and is executable.

To make the script executable use ``chmod +x <hook_script>``

Disabling the hooks
-------------------

To disable the script you can add the extension ‘.sample’ to the hook
script.
