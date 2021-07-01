# Detect license of Python modules

Assigned intern: Viliam Podhajecký
Assigned mentor: Frido Pokorny

## Project Goal
The goal of this project is to detect license of Python modules.

## Deliverables

A Jupyter Notebook, later an CLI application, that can automatically detect
license information of Python modules. This CLI application is then integrated
into the system and automatically detects license information of Python modules
analyzed.

## Prerequisites for Team Members
Please check you have all the following:

* Access to Red Hat network
* Access to GMail and Google Chat
    * Be part of Thoth-Station Google Chat Room
* Be part of Thoth scrum meetings
    * You should receive an invite to a Google calendar Event
* Access to GitHub using your GitHub your account
    * Thoth Station
* Get access to JupyterHub
    * https://odh.operate-first.cloud/

## Project outline
1. Welcome to the Thoth Station!

    1. get familiar with team members

2. Get familiar with thoth-solver [1], study its output

3. Get access to solver dataset that is present on Ceph, explore the dataset
   using Jupyter Notebooks, create a batch of solver documents

    1. You can also check available datasets on Kaggle [2] and GitHub [3]

4. Design and propose a solution that will automatically or semi-automatically
   classify license of Python modules, discuss the proposed solution with the
   team

    1. Discuss algorithm used and source of license information

    2. Check existing solutions that work with solver dataset ([4] and [5]) and
       study how they work to acquire possible inspiration

    3. Check license information in package metadata (eigher in ``license``
       field or check license specific trove classifiers) - see [7], [8] and
       [9] for more info

5. Create a generic Jupyter Notebook that accepts a list of solver documents
   and extracts license information

6. Convert the created Jupyter Notebook into a CLI

7. Discuss correctness and applicability of the proposed solution

8. Integrate the created CLI into the system ("solver" workflow)

9. Sync license information into the database (see thoth-storages module)

10. Design a wrap adviser pipeline unit [6] in adviser that provides license
   information to users

## Stretch goals

* Detect and infer license information from dual licensed projects

## References

1. https://github.com/thoth-station/solver/
2. https://www.kaggle.com/thothstation/thoth-solver-dataset-v10
3. https://github.com/thoth-station/datasets
4. https://github.com/thoth-station/prescriptions-gh-release-notes-job
5. https://github.com/thoth-station/solver-project-url-job/
6. https://thoth-station.ninja/docs/developers/adviser/wraps.html
7. https://packaging.python.org/guides/distributing-packages-using-setuptools/#license
8. https://packaging.python.org/guides/distributing-packages-using-setuptools/#classifiers
9. https://pypi.org/classifiers/
