# Versioning and code integration

This area captures the general approach we take with versioning products developed by the ENF. This is not a strict rule that is applied to every single product or code repository within the GitHub organization. It is meant more as a general guideline but the rules may be enforced more strictly for specific products (or suite of products) within the organization.

This area also captures the git branching strategy to follow when developing patches to software that may impact multiple versions of the software. In addition, it also covers details related to the recommended approach of integrating into a single repository the different products or libraries that are needed as dependencies.

## Versioning guidelines

We use [semantic versioning](https://semver.org/). Initial releases of a major version will be proceeded by one or more pre-release versions. Pre-release versions, know as release candidates, use the identifier `rc[0-9]+`.

## Code Merge Standards and Processes

Main must be releasable. Features should be merged when they are ready to be released. New features should be tested and approved.

### Merge Details
For a Pull Request (PR) identify the earliest Major/Minor release you are targeting.

* Start the PR name with the release in brackets example “[3.2] ”
* Merge into the earliest Major/Minor release
* Repeat the process for each subsequent release including the main branch

Example, fix for release 3.2.
<table>
  <tr>
   <td>Release Target
   </td>
   <td>Title
   </td>
   <td>Source Branch
   </td>
   <td>Target Branch
   </td>
  </tr>
  <tr>
   <td>3.2
   </td>
   <td>[3.2] My Fix
   </td>
   <td>myfix_feature_3.2
   </td>
   <td>release/3.2
   </td>
  </tr>
  <tr>
   <td>4.0
   </td>
   <td>[3.2 -> 4.0] My Fix
   </td>
   <td>myfix_feature_4.0
   </td>
   <td>release/4.0
   </td>
  </tr>
  <tr>
   <td>Next Release
   </td>
   <td>[4.0 -> main] My Fix
   </td>
   <td>myfix_feature_main
   </td>
   <td>Main
   </td>
  </tr>
</table>

### Special Situations to Note
* If the PR is targeted for the next release and there is no release branch, target the main branch.
* If the targeted release is beyond the next release, merge it into main, but protect it from general availability.
* If the feature is experimental and not ready for release, keep it in a feature branch, do not merge.
* Complex features may be broken up into smaller deliverables and merged into the main code base while maintaining backwards compatibility.

Example you have work targeted for release/5.0. Target the main branch when the following branches exist:
* release/3.2
* release/4.0
* main


## Code integration

TBD
