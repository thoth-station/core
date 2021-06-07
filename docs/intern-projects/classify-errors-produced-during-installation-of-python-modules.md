# Classify errors produced during installation of Python modules

Assigned intern: Bjoern Hasemann
Assigned mentor: Frido Pokorny

## Project Goal
The goal of this project is to create a classifier that can classify errors reported during Python package installation. This classifier will be used in thoth-solver errors classification as well as in build analysis.

## Deliverables
A Jupyter Notebook, later an CLI application, that can automatically classify error logs.

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
    * https://jupyterhub.datahub.redhat.com/

## Project outline
1. Welcome to the Thoth Station!
    1. get familiar with team members
2. Get familiar with thoth-solver [1], study its output
3. Get familiar with micropipenv [2], study its output
4. Get familiar with Amun service and inspections that are run there [4]
5. Get access to solver dataset that is present on Ceph, explore the dataset using Jupyter Notebooks, create a batch of solver documents that capture failed solver runs with the error log reported
    1. You can also check available datasets on Kaggle [3] and GitHub [4]
6. Similarly to the previous point, get access to inspection dataset
7. Design and propose a solution that will automatically or semi-automatically classify errors, discuss the proposed solution with the team
    1. Discuss algorithm used
    2. Discuss how the solution can be applied to solver errors and errors in inspection build logs
8. Create a generic Jupyter Notebook that accepts a list of solver documents and classifies them automatically
    1. Check already implemented classifier, propose improvements or reuse parts
9. Create a generic Jupyter Notebook that accepts a list of inspections and automatically classifies them
    1. Discuss how the error is extracted
    2. Study buildlog-parser, think of its reusability [6]
10. Discuss correctness and applicability of the proposed solution

## Stretch goals:
* Study solver workflow and how it works in Thoth deployment, try to come up with a design on how to integrate your solution into solver workflow
* Integrate your solution into solver workflow
* Extend error classification to classify also errors specific to Amun inspections (e.g. failed push of images)
* Study buildlog analysis endpoint and build analysis workflow
* Integrate your solution into buildlog analysis workflow

## References
1. https://github.com/thoth-station/solver/
2. https://github.com/thoth-station/micropipenv
3. https://www.kaggle.com/thothstation/thoth-solver-dataset-v10
4. https://github.com/thoth-station/datasets
5. https://github.com/thoth-station/amun-api/
6. https://github.com/thoth-station/buildlog-parser
7. https://github.com/thoth-station/report-processing

## Previous attempts to learn from
* sraghura
    * https://bluejeans.com/playback/s/z6ZEf27gKasWfJqXtkzJYkg1YpwnBcTDLkB9TLYuU5SSgaDVi51tYIlAtyfCKDeW
    * https://github.com/thoth-station/notebooks/blob/master/notebooks/development/Solver%20error%20classification.ipynb
* skotak
    * https://docs.google.com/document/d/1SAzyxxfXpRf7bnuuF4Eva6EXXdUcRqWhrfBOYQfiWk8/edit#
    * https://docs.google.com/presentation/d/1lB4GBAvhp6ZFbafgYvBGnf1C-aTjzkXK0VrOfs_Skxo/edit#slide=id.g8c299ddf99_1_950
    * https://bluejeans.com/s/8UYPQ
    * https://docs.google.com/presentation/d/1bVXHEvTojSXzSlUcrRNS3DcT_NeSg0nvZcREDUIHPBs/edit#slide=id.g8c299ddf99_1_950
