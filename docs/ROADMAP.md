# Thoth Roadmap

After the current and coordinated release of Thoth's components, we started this document to outline our
current focus areas and the major items we are working on.

For a more detailed overview of our current activities, have a look at our GitHub projects. We use them to plan our
sprints.

* [Planning Board](https://github.com/orgs/thoth-station/projects/31)
* [SIG DevSecOps](https://github.com/orgs/thoth-station/projects/16)
* [SIG Observability](https://github.com/orgs/thoth-station/projects/18)
* [SIG Stack Guidance](https://github.com/orgs/thoth-station/projects/35)
* [SIG User Experience](https://github.com/orgs/thoth-station/projects/40)

## Informative Advice

Based on a [command line tool](https://github.com/thoth-station/thamos/) and our
[GitHub App](https://github.com/marketplace/khebhut) we will extend the advice we give to human developers. This
extension will not only broaden the coverage of Python packages known by Thoth, but also include tips how to deploy
Python-based machine learning and data science applications.

The command-line tool is the base for Optimizing Deployment Pipeline.

## Reproducible Deployment Pipeline

Integrating Thoth's advise service, we create an optimizing and reproducible deployment pipeline for intelligent
applications running on OpenShift. This will select the best possible (based on Thoth's knowledge graph) application
stack, apply runtime specific configuration, and will optimize machine learning models if possible.

## Pipelines for Reproducible Builds

As a foundation to the [Open Data Hub](http://opendatahub.io/) and the Optimizing Reproducible Deployment Pipelines,
we host build pipelines for CUDA-enabled Jupyter Notebook container images, Thoth-enabled Python 3.6 and 3.8 builder
images and Tekton Pipeline Tasks, and accompanying documentation how to replicate these on-premise or OpenShift
deployments operated by our customers and partners.

## Thoth Services

The following section describes the services we provide to open source projects.

### Kebechet GitHub Application

[Khebhut (or Kebechet)](https://github.com/marketplace/khebhut) is a GitHub Application we provide on GitHub's
marketplace. It is gathering information, advice and justification based on Thoth's Knowledge Graph per Pull Request
opened for each repository the application is enabled for. With this information presented as a Check Status, we
hope to educate human developers on their software, the changes they do in that specific pull request and what our
advice is (based on the existing knowledge). Each repository containing a Python application that is unknown to Thoth
will be used to learn new observations, as Thoth automatically extends its Knowledge Graph.

### Thamos command-line tool

Thamos is our command-line tool to access Thoth's Knowledge Graph, it could be run on a local directory and give
advice without hosting a repository on GitHub.

### Build Pipeline repository

Thoth's build pipeline repository, or Tekton Task repository, is our contribution to the
[Tekton catalog](https://github.com/tektoncd/catalog), and enables Python application developers to integrate
Thoth Service consuming tasks (for example a Python module provenance check, or Security report) into their OpenShift
and Tekton Pipelines.

### Jupyter Requirements Management

Jupyter tools focused on the Data Scientist workflow have been created to help them with dependencies management:

* Jupyter Notebook extension [jupyter-nbrequirements](https://github.com/thoth-station/jupyter-nbrequirements)

* JupyterLab extension [jupyterlab-requirements](https://github.com/thoth-station/jupyterlab-requirements)

They feature similar functionality as thamos, but embedding the dependencies and the locked dependencies within the meta information
of the Jupyter Notebook file itself together with creating dependencies files in the requested requirement formats.
