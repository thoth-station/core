# Sesheta Cronjobs

This is a set of OpenShift CronJobs that support the Thoth-Station Organization on GitHub as a cyborg team member.

## Install

Set the following environment variables

 * K8S_AUTH_HOST
 * K8S_AUTH_VERIFY_SSL
 * K8S_AUTH_API_KEY
 * SESHETA_GITHUB_ACCESS_TOKEN

Use the Ansible playbook `deploy-sesheta-cronjobs` to create a project and deploy the CronJobs.