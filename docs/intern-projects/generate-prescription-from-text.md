# Generate prescriptions from text (text2prescription)

Assigned intern: ??
Assigned mentor: ??

## Project Goal
The goal of this research project is to create text2prescription model that can be used in a bot for generating prescriptions to heal Python Projects from text inputs.

## Deliverables
A Jupyter Notebook, later an CLI application, that can automatically generate prescriptions from text input.

## Prerequisites for Team Members
Please check you have all the following:

* Access to Operate First
* Access to GMail and Google Chat
    * Be part of Thoth-Station Google Chat Room
* Be part of Thoth scrum meetings
    * You should receive an invite to a Google calendar Event
* Access to GitHub using your GitHub your account
    * Thoth Station
* Get access to JupyterHub
    * https://odh.operate-first.cloud/

## Project outline
1. Welcome to the Thoth Station! [1]
    1. get familiar with team members
2. Get familiar with adviser [2], study how it works [3].
3. Get familiar with prescriptions [4] [5], study how they are created [6].
4. Research methods for mapping text to templates (e.g. prescription).
5. Create NLP pipeline to analyze Text inputs (using Elyra [7] and Kubeflow Pipelines[8] available on Operate First).
6. Create NLP model for entity recognition from text specific to prescriptions. (e.g. Python package, runtime environment, hardware).
7. Create a Jupyter Notebook that accepts text and produce prescription (.yaml format).
    1. Discuss NLP pipeline steps.
    2. Discuss NLP model for entity recognition specific to prescriptions.
8. Discuss applicability and use of this new approach (e.g. bot supporting users that want to create a prescription for Python application)

## Stretch goals:
* Create a bot that can receive text from an issue as input and create a pull request with prescriptions

## References
1. https://thoth-station.ninja/
2. https://github.com/thoth-station/adviser
3. https://developers.redhat.com/articles/2021/09/22/thoth-prescriptions-resolving-python-dependencies#
4. https://github.com/thoth-station/prescriptions
5. https://thoth-station.ninja/docs/developers/adviser/index.html#pipeline-units
6. https://www.youtube.com/watch?v=OCX8JQDXP9s
7. https://github.com/elyra-ai/elyra
8. https://www.kubeflow.org/docs/components/pipelines/overview/pipelines-overview/
