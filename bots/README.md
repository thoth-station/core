# Sesheta Cronjobs

This is a set of OpenShift CronJobs that support the Thoth-Station Organization on GitHub as a cyborg team member.

## Install

Set the following environment variables

 * K8S_AUTH_HOST
 * K8S_AUTH_VERIFY_SSL
 * K8S_AUTH_API_KEY
 * SESHETA_GITHUB_ACCESS_TOKEN

Use the Ansible playbook `deploy-sesheta-cronjobs` to create a project and deploy the CronJobs.

# Known Issues

The Ansible playbooks do not work

You need to create secrets for hook manually:

```
oc create configmap plugins --from-file=plugins=config/plugins.yaml
oc create configmap config --from-file=config=config/config.yaml

```

Create a Ultrahook deployment manually: `oc process --namespace=aicoe ultrahook --param=ULTRAHOOK_SUBDOMAIN=bots-prod --param=ULTRAHOOK_DESTINATION=https://hook-aicoe-prod-bots.cloud.upshift.engineering.redhat.com/hook`
