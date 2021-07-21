# Bootstrap database of Thoth prescriptions

Assigned intern:
Assigned mentor:

## Project Goal

The goal of this project is to extend the current database of prescriptions
with known or not yet known issues in the Python ecosystem.

## Deliverables

Set of YAML files committed to
[thoth-station/prescriptions](https://github.com/thoth-station/prescriptions)
repository that help the recommender system to advise better software stacks to
users.

## Prerequisites for Team Members

Please check you have all the following:

* Be part of Thoth-Station Google Chat Room
* Be part of Thoth scrum meetings
    * You should receive an invite to a Google calendar Event
* Access to GitHub using your GitHub your account
    * Thoth Station

## Project outline
1. Welcome to the Thoth Station!
    1. get familiar with team members
2. Get familiar with [thoth-station/prescriptions](https://github.com/thoth-station/prescriptions) repository
3. Get familiar with prescriptions concept, follow the [online documentation for more info](https://thoth-station.ninja/docs/developers/adviser/prescription.html)
4. Identify popular Python packages that can be valuable to data scientists and Python developers
    1. Take a look at already existing [hundredsDatasciencePackages](https://github.com/thoth-station/init-job/blob/master/hundredsDatasciencePackages.yaml) list
    2. Take a look at Python packages based on their popularity (number of downloads from PyPI)
5. For the identified set of Python packages create prescriptions that add knowledge to the recommender system so that users do not encounter known issues
    1. Follow project issues and/or project release notes
    2. Collaborate with communities to understand issues and required fixes, present prescriptions concept to communities
6. Get familiar with [Amun](https://github.com/thoth-station/amun-api) service and [Dependency Monkey](https://thoth-station.ninja/docs/developers/adviser/dependency_monkey.html)
7. Identify possible cases that are suitable for running Dependency Monkey to spot issues in packages or runtime environments
8. Run Dependency Monkey jobs and/or Amun inspections to conduct experiments that can result in new prescriptions
    1. Discuss possible issues with upstream communities
10. Discuss extensibility and possible improvements that would help you to get results more effectively

## References

1. https://github.com/thoth-station/prescriptions
2. https://thoth-station.ninja/docs/developers/adviser/prescription.html
3. https://thoth-station.ninja/docs/developers/adviser/dependency_monkey.html
4. https://github.com/thoth-station/amun-api
