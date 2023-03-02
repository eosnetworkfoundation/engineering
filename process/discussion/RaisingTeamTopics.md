# How To Raise a Topic to the Team

This document reflects the living process by which the ENF engineering team raises, discusses, and resolves topics that require team consensus.

## What Topics are Appropriate

This process applies to any topic of discussion where the stakeholders are exclusively members of the ENF engineering team. This does not imply 
that the decisions cannot have impacts outside the team. However, any impacts should be limited such that they do not materially affect users' or
other internal parties ability to interact with our product or services. 

For example:

### In Bounds Topics
* Refactoring systems that are difficult to maintain or iterate.
* Adjusting dependencies and/or versions.
* Building consensus on engineering's inputs to the product team's vision for the product.
* This process (or any team process) itself.

### Out of Bounds Topics
* Creation of new product lines
* Removal of critical information other departments depend on (like documentation)

## Process

### Creating a new Topic

Topics are stored as issues in this repository. They must:
* Be labeled with `decision+🤔`. 
* Have a concicse subject that relates to the topic.
* Have a description that poses a question or hyopthetical.
* Provide any additional supporting material.

### Selecting Topics for Live Discussion

During our weekly engineering meeting we will review topics from the [list of issues labeled as `decision+🤔`](https://github.com/eosnetworkfoundation/engineering/issues?q=is%3Aissue+is%3Aopen+label%3A%22decision+%F0%9F%A4%94%22) 
This list is sorted by the number of :+1: reactions the issue has received.

#### The Clock
Issues will be given a 10 minute maximum window in the live meeting for discussion. If a resolution is not found within the allotted time it is tabled and can be
brought back up in future meetings.

#### Exceptions
There are (2) exceptions to this selection process:
1. Executive Decree - @wanderingbort reserves the right to promote a topic to the live discussion regardless of its :+1: count.
2. Volunteer Mediator - as described below if an issue has a volunteer mediator it will be prioritized above issues without.

#### Summary
The resulting priority will be:
1. [Issues with "Executive Decree" ordered by vote](https://github.com/eosnetworkfoundation/engineering/issues?q=is%3Aopen+is%3Aissue+assignee%3Awanderingbort+label%3A%22decision+%F0%9F%A4%94%22+sort%3Areactions-%2B1-desc)
2. [Issues with mediators ordered by vote](https://github.com/eosnetworkfoundation/engineering/issues?q=is%3Aopen+is%3Aissue+assignee%3A%2A+label%3A%22decision+%F0%9F%A4%94%22+sort%3Areactions-%2B1-desc)
3. [Issues without mediators orderd by vote](https://github.com/eosnetworkfoundation/engineering/issues?q=is%3Aopen+is%3Aissue+no%3Aassignee+label%3A%22decision+%F0%9F%A4%94%22+sort%3Areactions-%2B1-desc+)

### Volunteer Mediator
In an effort to make decisions more efficiently and provide an opportunity for team members who excel at facilitating decisions to provide a team-wide benefit, 
Volunteer Mediators can elect to assign any open issue to themselves.

#### The Purpose of a Mediator
Mediators pick up extra tasks outside of the live meeting. Their purpose is to use the time outside the meeting to work with stakholders and undrestand the crucial
parts of the decision at hand. During the live meeting, the mediator will have control of the floor for the allotted time. They may, at their descretion, present
material, call upon stakeholders to comment, or any other action that is meant in good faith to drive the discussion.

The goal of a mediator should be to compress what would otherwise be a lengthy live decision making process into the short time alotted during the live meeting.

##### :warning: Mediators should strive to be unbiased. However, it will be impossible to be a truly unbiased mediator. We, as a team, should accept that risk in trade for the potential efficiency gain. 
