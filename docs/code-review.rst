Code Review
-----------

For all our projects of the `Thoth
Station <http://thoth-station.ninja/>`__ we require code reviews before
merging the code. We use `Zuul <https://zuul-ci.org/>`__ to implement
`project gating <https://zuul-ci.org/docs/zuul/user/gating.html>`__.

Code is merged by zuul, but before a pull request is merged, zuul runs
all project specific jobs of the so called ‘gate pipeline’. If all jobs
are successful, code is merged. If a job fails, the pull request will
get a comment added and the pipeline finishs without merging.

The requirements and triggers for the gate pipeline are defined by
`zuul-config’s gate
pipeline <https://github.com/thoth-station/zuul-test-config/blob/master/zuul.d/_pipelines.yaml#L45-L55>`__:

Requirements
~~~~~~~~~~~~

The following requirements must be met to start merging a Pull Request:

-  a ‘approved’ `GitHub
   review <https://help.github.com/articles/about-pull-request-reviews/>`__
   must exist
-  the ‘approved’
   `label <https://help.github.com/articles/about-labels/>`__ must be
   set
-  `thoth-zuul <https://github.com/apps/thoth-zuul>`__\ ’s local/check
   must be successful

Triggers
~~~~~~~~

Whenever the Pull Request changes state, Zuul reevaluates if the
Requirements to run the jobs ob the gate pipeline are met.
