Code Review
-----------

For all our projects of the `Thoth Station <http://thoth-station.ninja/>`__ we
require code reviews before merging the code. We use `Prow <
https://github.com/kubernetes/test-infra/tree/master/prow >`__ to implement
project gating with `Tide
<https://github.com/kubernetes/test-infra/blob/master/prow/cmd/tide/README.md>`__.


Code is merged by prow, but before a pull request is merged, Prow runs
all project specific jobs of the so called ‘gate pipeline’. If all jobs
are successful, code is merged. If a job fails, the pull request will
get a comment added and the pipeline finishs without merging.


Requirements
~~~~~~~~~~~~

The following requirements must be met to start merging a Pull Request:

-  a ‘approved’ `GitHub
   review <https://help.github.com/articles/about-pull-request-reviews/>`__
   must exist
-  the ‘approved’
   `label <https://help.github.com/articles/about-labels/>`__ must be
   set
-  Prow's local/check must be successful

Triggers
~~~~~~~~

Whenever the Pull Request changes state, Prow reevaluates if the
Requirements to run the jobs ob the gate pipeline are met.


Prow configuration
~~~~~~~~~~~~~~~~~~
See https://github.com/operate-first/apps/blob/master/prow/overlays/smaug/config.yaml
