# Project Thoth Naming Schema for Images

* Status: proposed
* Date: 2021-Jun-17

Technical Story: As Thoth goal to provide curated stack and images, it would be nice to have a convention for naming of the images.

## Context and Problem Statement

Image names are important for branding and let others identify easily a specific image they need. For example "I want to work on computer vision project with Tensorflow, what stack and image should I use?" Having a trusted well maintained source of images with clean naming convention can help on that.

## Considered Options

* `s2i-{application}`
* `odh-{application}`
* `curated-stack-{application}`

These names are for the core repository name, then `overlays` will allow for combinations of libraries based on other criteria, for example `ml_framework` or `hardware`:

    `odh-nlp`
    ├── overlays                    # Overlays structure for builds
    │   ├── odh-nlp-tensorflow          # NLP image with TensorFlow ML framework
    │   ├── odh-nlp-tensorflow-gpu      # NLP image with TensorFlow ML framework for GPU
    │   ├── odh-nlp-pytorch             # NLP image with Pytorch ML framework
    │   ├── odh-nlp-pytorch-gpu         # NLP image with Pytorch ML framework for GPU
    │   └── odh-nlp-scikit-learn        # NLP image with Scikit-learn ML framework
    └── ...

## Decision Outcome

Chosen option: for branding/marketing having ODH in front seems to be the best solution, in this way the name will be shorter as well.

### Positive Consequences <!-- optional -->

* users can immediately select an image based on the application they want.
* using overlays we can have a variety of combination, not just for ml_framework

### Negative Consequences <!-- optional -->

* N/A

<!-- markdownlint-disable-file MD013 -->
