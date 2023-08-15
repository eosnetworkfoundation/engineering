# Assigning issues and pull requests to milestones

This document captures the process of when and how to assign a milestone to an issue or pull request (PR).

## Types of milestones

Our repos typically have a milestone that tracks an upcoming version to be released of the product tracked by the repo. Some repos may have more granular milestones leading up to the next minor/major version of the product.

The milestones can be divided into three categories:

* Patch milestone: A patch milestone tracks a patch release of the product which is meant to only contain bug fixes and no new features. The patch milestone is typically named following a pattern where it has a prefix referring to the name of the product followed by a version number `X.Y.Z`. The `Z` number refers to the patch version number which is incremented as part of the new release. It is also possible for a patch milestone to track a release candidate version other than the initial `rc1` release; in this case the version would be something like `X.Y.0-rc2`.

* Feature milestone: A feature milestone tracks features that must be integrated into the `main` branch of the repo prior to a code freeze and branch cut which will establish the `release/X.Y` branch for to the to be released version of the product that increments either the major version number (`X`) or the minor version number (`Y`). The feature milestone is typically named following a pattern where it has a prefix referring to the name of the product followed by a version number `X.Y.Z`. But it is possible the milestone may use other names to track specific features as part of a granular milestone.

* Release milestone: A release milestone tracks the initial release candidate of a release of the product with either a major or minor version bump. The release milestone is typically named following a pattern where it has a prefix referring to the name of the product followed by a version number `X.Y.0-rc1`.

## Assigning milestones to issues

Every issue that has as part of its definition of done the delivery of code changes integrated into the `main` branch of a release branch (i.e. `release/X.Y`) must have a milestone assigned to it before it is added into the current sprint and work on the issue begins. Ideally, the milestone would be assigned to the issue during the backlog refinement meeting prior to even the iteration (sprint) planning meeting.

If an issue tracks a bug fix in a released stable version of the product, then it should have a `bug` label assigned and the team should come to a conclusion for how far back of a version (the oldest support version of the product) the bug fix should target. This determines the patch milestone to assign to the issue. For example, consider a scenario within the `leap` repo where where versions 3.2 and 4.0 of Leap are supported while the `main` branch is tracking work for an upcoming 5.0 release. If a bug is discovered that impacts code as old as version 3.2, the issue may be assigned a milestone `Leap 3.2.Z` (where `Z` is replaced by the next available patch version number within the 3.2 series that has yet to be released). This also signals to the developer that they must first target to bug fix to the `release/3.2` branch, then bring the fix forward to the `release/4.0` branch, and then finally bring the fix forward to the `main` branch. If another bug is discovered that impacts version 4.0 but not any older versions, then the issue may be assigned a milestone `Leap 4.0.Z` (where again `Z` is set appropriately to the next available patch version number in the 4.0 series).

If an issue tracks a bug fix in a release candidate or it includes other refinements to the release candidate prior to the stable release, e.g. documentation updates, then it should be assigned the appropriate release milestone. For example, consider work on top of a recently released Leap 5.0.0-rc1. If a bug was discovered in Leap 5.0.0-rc1 that requires a new release candidate to test, then the issue tracking the bug would be assigned the `Leap 5.0.0-rc1` milestone. There may also be some issues that are not considered bugs but must be completed prior to being able to release a stable version of 5.0.0; those issues would be assigned the `Leap 5.0.0` milestone.

If an issue is not a bug fix or changes for an existing release candidate, e.g. if it is an enhancement or new feature, then it should be assigned the appropriate feature milestone. For example, consider a scenario within the `leap` repo where the `main` branch is tracking work for an upcoming 5.0 release of Leap. A new issue tracking a new feature for 5.0 would likely be assigned the `Leap 5.0.0-rc1` milestone, unless there is a more granular milestone for it that is more appropriate.

## Assigning milestones to PRs

Pull requests typically should not have milestones attached to them. The only exception is for the PRs that forward bug fixes from a release branch forward to another release branch. In that case, the PR forwarding to a release branch should be assigned a patch milestone corresponding to the version of the target release branch.

So consider again the scenario described earlier within the `leap` repo where where versions 3.2 and 4.0 of Leap are supported while the `main` branch is tracking work for an upcoming 5.0 release. 

The bug fix targeting Leap 4.0 first would involve two PRs. The first would be a PR targeting the `release/4.0` branch with the bug fix. A milestone should not be added to this PR because it would be redundant. The PR should be linked to the issue tracking the bug fix and that issue is already assigned to the `Leap 4.0.Z` patch milestone. The second PR would be targeting the `main` branch and would be bringing forward the bug fix that was merged into `release/4.0`. A milestone should not be assigned to this second PR either. The next major/minor release (Leap 5.0 in this scenario) would not be released until bugs have been fixed in patch release prior. So adding a milestone to the PR would just be polluting the milestone for the major/minor release with noise that make it more difficult for people to get to what they actually care about when looking at that milestone: the enhancements and new features that are part of a new major/minor release.

The bug fix targeting Leap 3.2 first would involve three PRs. The first would be a PR targeting the `release/3.2` branch with the bug fix. Again, a milestone should not be assigned to this PR since it would be redundant with the linked issue that is already assigned to the appropriate patch milestone.The second PR would be targeting the `release/4.0` branch and would be bringing forward the bug fix that was merged into `release/3.2`. The appropriate patch milestone should be assigned to this second PR; in this case, it would be a milestone named something like `Leap 4.0.Z`. Finally, the the third PR would be targeting the `main` branch and would be bringing forward the bug fix that was merged into `release/4.0`. Again, this third PR, since it is targeting `main`, should not have a milestone assigned to it.
