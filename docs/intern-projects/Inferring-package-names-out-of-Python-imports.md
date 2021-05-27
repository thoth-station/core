# Inferring package names out of Python imports

Assigned intern: Tlegen
Assigned mentor: Francesco Murdaca

## Project Goal
The goal of this project is to create an automated mechanism for inferring package names out of their imports.

## Deliverables
An endpoint on User API that can suggest package names based on an import supplied.

## Prerequisites for Team Members

Please check you have all the following:

* Be part of Thoth-Station Google Chat Room
* Be part of Thoth scrum meetings
* Access to GitHub using your GitHub your account: [Thoth Station](https://github.com/thoth-station)

## Project outline

0. Welcome to the Thoth Station!
1. Get familiar with [how we work](https://github.com/thoth-station/core/blob/master/README.rst)
    1. Get familiar with team members
2. Get familiar with [thoth-solver](https://github.com/thoth-station/solver/), study its output
3. Get familiar with [invectio](https://github.com/thoth-station/invectio), study its output
4. Check available results of thoth-solver runs that are present on Ceph, use Jupyter Notebooks to explore the dataset
    1. Make sure you have access to Ceph and data are readable
5. Check packages in the ecosystem that provide modules under a different name than the package name itself
    1. See import sklearn vs pip install [scikit-learn](https://pypi.org/project/scikit-learn/)
6. Design and propose a solution that can automatically derive module names
    1. No need to strictly use thoth-solver data if a better solution is found
    2. Mind "namespaced" modules
7. Write a program that can automatically derive package names out of imports
    1. Design a database that can hold such information, if needed
    2. Design an approach to sync required data into the database
8. Get familiar with Thoth deployment, design and propose integration of your application into the system
    1. Study Argo workflows, check how the proposed solution can be integrated into the system (e.g. run it after solver finishes)
9. Integrate your solution into Thoth
    1. Adjust templates in thoth-station/thoth-application repository
    2. Provide an endpoint on [user-api](https://github.com/thoth-station/user-api/) that can give information to users about imports Input: import Output: Package name (package required to be installed so that import works)
10. Create an [integration test](https://github.com/thoth-station/integration-tests/) verifying the endpoint implemented

## Stretch goals

* Create a small Python application that can check how similar two project names are, discuss its usability for detecting typosquatting
* Create a new Kebechet manager using new logic (https://github.com/thoth-station/kebechet/issues/727) 