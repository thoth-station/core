# Terms and Conditions for the Thoth Station Scrum

Thoth Station Inhabitants, v0.4.0, 2022-05-04

A scrum sprint (or iteration) is 3 weeks of calendar time, and a task should/can not span more than one sprint.
If a task can not be accomplished in one sprint it must be broken up.

Tasks are tracked as GitHub issues. Issues are created by anyone in the
community, including the team and the users of the Thoth service.

Issues are assigned to persons (they become an assignee of the issue) when a
person picks up the card and starts working on it (pulls it into the ‘in
progress’ list).

An Issue must meet minimum [quality standards](#quality) before it can be worked.

We have a list of [Github Projects](https://github.com/orgs/thoth-station/projects) to cluster issues into contexts, there is no hard requirement that all issues must be on a project, some of them can just stay
within a repository.

Issues are managed on GitHub, we use [labels](../community/labels.md).

Issues can belong to one of Thoth's [Special Interest Groups (SIGs)](../community/sig-list.md). These should have the corresponding `sig/` label and be tracked in the corresponding SIG's project.

<a name="triage"></a>
# Issue triage

Everyone is encouraged to assist in making sure every issue meets good quality standards, starting with the person who creates the issue.

The process of issue triaging involves making sure that the issues have enough quality.

Issues relevant to a particular SIG should be placed in that SIG project board,
in the New column.

Ultimately, SIGs are responsible for ensuring that the issues relevant to their SIGs have an adequate quality.

<a name="quality"></a>
## Criteria for good issue quality

A *good quality issue* is one that contains all the information and metadata
that enables everyone to properly understand it and put it in context, and
allows the team to plan it and work on it with the confidence that it will be
properly resolved.

The information that an issue should contain so that it is properly understood
depends on the type of the issue. Guidelines for each type are provided below.

In any case, every issue should have some metadata:

* the *type* of the issue, expressed with a label `kind/*`, for example `kind/feature` or `kind/bug`
* the *priority* it has: a label `priority/*`
* what *SIG* it belongs to, also a label `sig/*`
* categorization if it is a `[spike]`
* a measure of complexity (story points)/time estimate (see [effort estimates](#estimates) below)
* links to References: other relevant issues this relates to, prior art, external documents

Feature requests should contain:

* a User Story
* list of high-level Acceptance Criteria/Goals (that is signed off by the team, and unchangeable)
* checklist of detailed Acceptance Criteria (that might extend over the lifetime of the card)
* might have a due date assigned and confirmed by the team lead

Bug reports should contain:

* reproducer steps
* expected behavior and actual behavior
* environment information: components involved and their versions, details of the execution environment

Links to PRs that are implementing/fulfilling the acceptance criteria should be included as a comment on the issue. This can be handled automatically by referencing the issue from the relevant PR(s).

In any case, a clear reference must be present when the issue is closed, e.g. to
the PRs that implemented the issue, or an explanation of why it was discarded.

## Priorities

An issue’s priority is mainly derived from its relation to a key result, but could also be influenced by the team.

Applying any "priority/" label is only ok before the backlog refinement session, it shall indicate that the card is
important to the team, or important to support an upcoming key result. During the refinement session, the issue should
be planned accordingly.

### Zero-bug policy

In order to simplify planning, we implement a zero-bug policy. This means that
we prioritize bugs above all other issues, **for a certain definition of bug**.
During triage, SIGs should label sufficiently problematic issues (how they
determine that is up to the SIGs) with `kind/bug`. These issues are prioritized
for the next sprint.

Other "bugs" (somethings does not work as it should) should be requalified. #TODO: as what

If an issue seems to be both a bug and something else, it might indicate that it
needs to be split.

<a name="estimates"></a>
## Effort Estimates

The team estimates how much effort each issue is expected to require. The result of the estimation is a number within a Fibonacci series.

Here is a general guideline for the meaning of each value:

| Story points | Complexity                                                                          | Risk                                   | Uncertainty                                                             | Effort                                                                               |
|--------------|-------------------------------------------------------------------------------------|----------------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
|            1 | Extremely simple to do. There is a minimal amount of work that needs to be done.    | Low                                    | None                                                                    | Very little effort needed                                                            |
|            2 | Very simple to do. The acceptance criteria are short and can be satisfied with ease | Low                                    | None                                                                    | Little effort needed                                                                 |
|            3 | Simple to do. The acceptance criteria are longer but clear and manageable.          | Low                                    | Little. Can still be done. May need to consult peers                    | It takes some time to complete                                                       |
|            5 | Doable, with a few aspects that may be difficult or long.                           | Medium - might need mitigation plan    | Little. Can still be done. May need to consult peers or other resources | Requires especial focus to complete                                                  |
|            8 | Doable but difficult or long                                                        | Medium - should have a mitigation plan | Medium. Pair programming is likely.                                     | It takes significant amount of sprint to complete this story                         |
|           13 | Hard. Difficult or complicated. There is a lot of work needed to satisfy this task. | High - must have a mitigation plan     | Medium. Task is on the border of needing a spike to investigate it      | Full time effort likely to take the whole sprint to complete                         |
|           21 | Impossible for a sprint. Task is too big, break into smaller tasks                  | Extreme - Should not be in a sprint    | High. Team has no idea. Create a spike                                  | The story takes significant effort and will require more than one sprint to complete |

# Issue life cycle

New issues are [triaged](#triage) by the team. This activity is driven by the
[Special Interest Groups (SIGs)](../community/sig-list.md) and contributors, and
coordinated in the [sprint meetings](#sprint).

When the team considers that an issue is well understood (i.e. has [good quality](#quality)) and it fits within the scope of the project, the issue gets labeled as `triage/accepted`. If there are missing details that prevent that, a `triage/needs-information` is added.

When the assignee starts to work on an issue, the issue is labeled `lifecycle/active`.

<a name="requirements"></a>
## Requirements for issues to be planned

An issue must meet the following criteria before it can be planned:

- have an assignee
- be `triage/accepted`
- have a defined priority that is aligned with the sprint goals

Feature requests (`kind/feature`) must also have:

- estimate points
- clear acceptance criteria

Having assignees and estimate points for all issues enables an assessment of the team's load for the sprint.

Having clear acceptance criteria is already a pre-requisite for issues to get
story points, actually, but this requirement is explicitly stated here due to
its importance, as it is what allows understanding if/when the task has been
properly completed.

<a name="sprint"></a>
# Sprint workflow and sprint meetings

Each sprint cycle, all the team gets together in a series of meetings to organize the work for the sprint.

## Backlog Refinement Session

Each [Special Interest Group (SIG)](../community/sig-list.md) refines the set and contents of the issues that are relevant to their SIG independently by triaging issues in the ‘new’ or 'backlog' columns of relevant [Thoth Station Projects](https://github.com/orgs/thoth-station/projects).

There are issues that require involvement from the whole team in order to be triaged. For example:

- issues that do not obviously align to a specific SIG
- new functionality that involves components from multiple SIGs
- important features that deserve team awareness and/or agreement
- any issue that requires clarification that can not be addressed individually

The goal of the backlog refinement session is to offer the space for the team to review these issues together.

The outcome of the backlog refinement session is a set of issues that are properly triaged, i.e. that are understood by the team by meeting the [issue quality](#quality) standards.

## Sprint Planning Session

SIGs pulls the `kind/bug` issues into the `next` list.

SIGs pull the issues which support the high-level team objectives/theme and key results into the ‘next’ list, so that the
team is clear of what is to be worked on in the next sprint.

Issues must meet the [quality requirements](#requirements) before they can be pulled into planning.

During the session, issues are open to allocation to any team member, and the team agrees to the interested team member
to work on the issue. If the interested team member needs to be trained to fulfill the task, then a
task has to be added for training required and taken by another team member who is knowledgeable of the topic. If the training task is not feasible, another team member should
take the initial task.

Being a team effort, each sprint aims to have a defined *sprint goal*, which is
a theme or topic that is common across multiple issues that form the
sprint. Setting a sprint goal helps guide the planning of which issues to
select, and it facilitates team work and coordination. Sprint goals are
documented in the corresponding [sprint release issue in the thoth-application repo](https://github.com/thoth-station/thoth-application/issues?q=is%3Aissue+label%3Aarea%2Frelease-eng+is%3Aopen).

The outcome of the sprint planning session is a set of issues that will be worked on by the team in the following sprint, most of which align to a common sprint goal.

## Scrum Standup

This activity is subject to review next! We want to broaden the communication and unfreeze the behaviours of a
multicultural geographically dispersed team.

How do we do that?
Maybe by asking: Can we achieve the scrum goal? Are you Blocked? Could someone help you? Can we demo all the tasks we
will have done at the end of the scrum? What can we communicate to the outside of the team at the end of the scrum?

## Sprint Demo

Scrum demos will be recorded and have meeting minutes. Every team member is encouraged to demo the work of the past
sprint. Demos are published to [our YouTube channel](https://www.youtube.com/channel/UClUIDuq_hQ6vlzmqM59B2Lw).

## Sprint Retrospective

This activity is for reviewing what went well/not well regarding the past sprint. A discussion like what was the better
aspect we would like to continue? What should be aspects that need more discussion as a team? What could have been a
better way to proceed?

The outcome of the sprint retrospective is a set of action items that will help the team improve in future sprints.
