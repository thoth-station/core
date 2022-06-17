# {short title of solved problem and solution}

* Status: proposed
* Deciders: @KPostOffice @fridex @cgoern <!-- optional -->
* Date: 2022-3-15 when the decision was last updated} <!-- optional -->

Technical Story: [Kebechet#873](https://github.com/thoth-station/kebechet/issues/873)

## Context and Problem Statement

Kebechet is being run too often and is eagerly eating resources in cluster. We need to pare down how often we spin up
pods to do repository management.

## Decision Drivers <!-- optional -->

* Less pods being spun up.
* Reduce frequency of reaching GitHub API quota limit

## Considered Options

* Option 1: Filter web-hooks in thoth-user-api
* Option 2: Create Kebechet deployment receives web-hooks and only runs specific manager(s) depending on contents
* Option 3: Create individual repositories and GitHub applications for each manager
* Option 4: create GitHub app for each repo and choose auth at run time

## Decision Outcome

Chosen option: "option 3", because we can use existing bot frameworks and github event handlers such as
`gidgethub`(Python) and `probot`(JavaScript). This should help reduce cluster load as pods will be shorter lived and
less frequent, however, it does require multiple small deployments for handling web-hooks.

Implementing option 2 and option 4 might be another good solution.

<!-- Please feel free to comment with your own opinions -->

### Positive Consequences <!-- optional -->

* Reduced resource consumption
* More apps means more quota
* Each app's behavior is well defined. It's at times unclear what "Kebechet" is

### Negative Consequences <!-- optional -->

* Follow up decisions required: "What technologies do we use?", "How do we manage configuration?"
* Transition from maintaining list of managers to installing individual managers

## Pros and Cons of the Options <!-- optional -->

### Option 1: Filter web-hooks in thoth-user-api

* Good, because it requires minimal upfront work
* Bad, because it introduces tight coupling between Kebechet and user-api
* Bad, because GitHub already only sends a subset of events and it is likely that we would not see a major decrease in
resource consumption.

### Option 2: Create Kebechet deployment receives web-hooks and only runs specific manager(s) depending on contents

* Good, because it allows for thorough processing of events prior to pod being spun up
* Good, it can still run multiple bots in the same pod (depends on implementation)
* ?, Preserves Kebechet name recognition (may obfuscate functionality)
* Bad, does not help with reducing GitHub API quota consumption

### Option 3: Create individual repositories and GitHub applications for each manager

* Good, because it creates more apps which effectively increases the total API limit
* Good, segregating functionality helps users understand what they are installing
* Good, workloads can be very selectively run through thorough web-hook processing
* Bad, many small deployments

### Option 2&4: Create Keb deployment and Individual apps

* Good, because it creates more apps which effectively increases the total API limit
* Good?, single deployment
* Good, workloads can be very selectively run through thorough web-hook processing
* Bad, installation story becomes unclear

<!-- markdownlint-disable-file MD013 -->
