# Sesheta Cronjobs

This is a set of OpenShift CronJobs that support the Thoth-Station Organization on GitHub as a cyborg team member.

In addition to that, there are playbooks helping with maintaining the source and parts of the build pipeline: SrcOps!

## Reset Build Pipeline

To reset a component to a stable state use `playbooks/reset_buildpipeline.yaml`. It will 

* reset the BuildConfig to use the master branch and push to the :test tag
* reset the ImageStreamTag :test to :stable
* redeploy the component

Example: `ansible-playbook reset_buildpipeline.yaml -e BUILD_CONFIG_NAME=user-api -e IMAGE_STREAM_NAME=user-api -e COMPONENT_NAME=user-api`

# Known Issues

You need to create secrets for hook manually:

```
oc create configmap plugins --from-file=plugins=config/plugins.yaml
oc create configmap config --from-file=config=config/config.yaml

```

Create a Ultrahook deployment manually: `oc process --namespace=aicoe ultrahook --param=ULTRAHOOK_SUBDOMAIN=bots-prod --param=ULTRAHOOK_DESTINATION=https://hook-aicoe-prod-bots.cloud.upshift.engineering.redhat.com/hook`
