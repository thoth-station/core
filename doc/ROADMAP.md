# Thoth Roadmap

After the current and coordinated release of Thoth's components, we started this document to outline our
current focus areas and the major items we are working on.

For a more detailed overview of our current activities, have a look at our GitHub projects. We use them to plan our
sprints.

* [Thoth Knowledge Graph](https://github.com/orgs/thoth-station/projects/8)
* [Amun](https://github.com/orgs/thoth-station/projects/12)
* [Investigator](https://github.com/orgs/thoth-station/projects/14)
* [Performance Indicators](https://github.com/orgs/thoth-station/projects/10)
* [Security Indicators](https://github.com/orgs/thoth-station/projects/2)
* [Adviser](https://github.com/orgs/thoth-station/projects/4)
* [Solver](https://github.com/orgs/thoth-station/projects/6)
* [Kebechet](https://github.com/orgs/thoth-station/projects/3)
* [User API](https://github.com/orgs/thoth-station/projects/7)

## Informative Advises

Based on a [command line tool](https://github.com/orgs/thoth-station/projects/3) and our
[GitHub App](https://github.com/marketplace/qeb-hwt) we will extend the advises we give to human developers. This
extension will not only broaden the coverage of Python packages known by Thoth, but also include tips how to deploy
Python-based machine learning and data science applications.

The command-line tool is the base for Optimizing Deployment Pipeline.

## Optimizing Deployment Pipeline

Integrating Thoth's advise service, we create an optimizing deployment pipeline for intelligent applications running
on OpenShift. This will select the best possible (based on Thoth's knowledge graph) application stack, apply
runtime specific configuration, and will optimize machine learning models if possible.

## Build Pipelines

As a foundation to the [Open Data Hub](http://opendatahub.io/) and the Optimizing Deployment Pipelines, we host build
pipelines for CUDA-enabled Jupyter Notebook container images, Thoth-enabled Python 3.6 and 3.8 builder images and
Tekton Pipeline Tasks, and accompanying documentation how to replicate these on-premise or OpenShift deployments
operated by our customers and partners.

## Thoth Services

The following section describes the services we provide.

### Kebechet GitHub Application

[Qeb-Hwt (or Kebechet)](https://github.com/marketplace/qeb-hwt) is a GitHub Application we provide on GitHub's
marketplace. It is gathering information, advises and justification based on Thoth's Knowledge Graph per Pull Request
opened for each repository the application is enabled for. With this information presented as a Check Status, we
hope to educate human developers on their software, the changes they do in that specific pull request and what our
advises is (based on the existing knowledge). Each repository containing a Python application that is unknown to Thoth
will be used to learn new observations, as Thoth automatically extends its Knowledge Graph.

### Thamos command-line tool

Thamos is our command-line tool to access Thoth's Knowledge Graph, it could be run on a local directory and give
advises without hosting a repository on GitHub.

### Build Pipeline repository

Thoth's build pipeline repository, or Tekton Task repository, is our contribution to the
[Tekton catalog](https://github.com/tektoncd/catalog), and enables Python application developers to integrate
Thoth Service consuming tasks (for example a Python module provenance check, or Security report) into their OpenShift
and Tekton Pipelines.
