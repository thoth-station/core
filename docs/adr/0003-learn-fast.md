# Thoth learns faster

* Status: proposed
* Date: 2020-Dec-02

Technical Story: Thoth learns faster and smart not randomly

## Context and Problem Statement

Currently Thoth uses graph-referesh-job to learn on unsolved packages, but they are scheduled randomly.
Moreover when adviser fails we learn about the missing packages to be solved only at the direct dependency layer (transitive one missing are still not known)
In User stack, direct and transtive one should be prioritized in learning by Thoth to be able to provide minimum postive advise (stack that can be locked and installed)

This description can be applied also to security packages not analyzed.

## Decision Drivers <!-- optional -->

* Time to have and entire dependency tree for a direct dependency solved and can be provide in advise.

## Considered Options

* Leave system as it is, graph-refresh continue to randomly pick packages to be solved from any solver and to be SI analyzed.
* graph-refresh becomes a secondary component that continue scheduling randomly for all solvers and another new component is created that find out which packages in the entire dependency tree are missing (querying the database? Or locking the software stack and listing all dependencies required till the last leaf of the tree) to be solved for a certain direct dipdendency for a certain runtime environment and schedule with priority solvers. In this way when asking for advise for a certain runtime environment the system will learn faster for the direct dependencies that are solved and for the transitive dependencies. This new component could be scheduled by investigator, use the logic to discover missing packages to be solved and send messages back to schedule solvers with priority for them ( maybe considering latest version and the one before to be scheduled first, rest will be in the hand of graph-refresh)

## Decision Outcome

Chosen option: new component that allow Thoth to learn faster with focus on specific software stack.

### Positive Consequences <!-- optional -->

* speed up learning focusing on specific packages for certain solver which are important for the user with priority.
* at init job level, we can have a clear estimate of the actual number of packages that needs to be solved to make advise at least able to lock a software stack as it would be done by pip or pipenv for certain dependency that have priority ( >100 data science packages) at their latest versions. Morever knowing the number of packages we can estimate based on learning rate the time required for the system to learn that.
* helps everytime a new solver is added, instead of waiting unkown number of time.
* helps because the combinations are multiple, also considering hardware combinations, and the time still remain unknown on when the system will learn that.
* improve user experience as we can estimate the time required dependending on the number of packages that still need to be solved by Thoth before providing that answer.

### Negative Consequences <!-- optional -->

* Overlapping a bit with graph-refresh which will remain to continue scheduling packages to be solved and SI analyzed.
