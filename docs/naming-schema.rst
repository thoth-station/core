Thoth Naming Schemata
=====================

Batch/manual and Cron Jobs
--------------------------

This section describes how to name certain objects related to batch and
cron jobs.

-  how to name image streams
-  how to name cronjobs
-  how to name buildconfigs

The CronJob shall just be called *dings*, so we get no redundancy when
we do ``oc get cronjobs``.

The ImageStream shall be called *dings* or *dings-job* as we can run the
image as a CronJob or via ``oc run`` manually or just once as a init pod
for some other deployment.

The BuildConfiguration will be named as the ImageStream it is outputting
to: *dings-job*.

The main container of the Pod created by the Job shall be called
*dings*, as he is carrying out the job. Any other container is
considered a side car and shall be named according to his function.
