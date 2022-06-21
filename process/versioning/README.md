# Versioning and code integration

This area captures the general approach we take with versioning products developed by the ENF. This is not a strict rule that is applied to every single product or code repository within the GitHub organization. It is meant more as a general guideline but the rules may be enforced more strictly for specific products (or suite of products) within the organization.

This area also captures the git branching strategy to follow when developing patches to software that may impact multiple versions of the software. In addition, it also covers details related to the recommended approach of integrating into a single repository the different products or libraries that are needed as dependencies.

## Versioning guidelines

TODO: What should our general versioning guidelines be? Do we distinguish between user-facing products versus development-focused libraries (and mostly interval vs external dev facing)? Do we want to push for semantic versioning?

### Versioning rules for the EOSIO product suite

TODO: Specific rules we have for the EOSIO product suite which includes nodeos, keosd, cleos, etc. as well as CDT and the system contracts (not clear if eosjs or other client libraries should be considered part of that core suite). Discuss hwo we want to maintain consistent major version across the products in the suite, but minor and patch versions remain independent.

## Branching strategy

TODO: Discuss `main` branch and `release/*` branches. Discuss how patches to `release/*` branches must be promoted in a particular way to `main`, with examples for clarity. What about building and testing for the next major release so that `main` can remain head of development even as we continuously integrate features for the next major (possibly breaking release) while still being ready to cut a new minor release as needed?

## Code integration

TODO: Discuss process for bringing in dependent libraries and tools into a project. Consider banning submodules and recommending git subtree merging instead? Where is a CMake external project appropriate?

