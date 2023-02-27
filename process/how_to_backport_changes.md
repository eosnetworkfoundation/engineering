### The process of back port changes to old release branches is as follows:

In order to back port changes to the old release branches you need to create your own branch,
push your changes to this branch, create a pull request with your changes and, when it will be approved,
merge your changes into the oldest release branch which you want to change.

Then you should create a branch that merges the previous release branch into the next release branch,
create a pull request and approve it. And do the same for each branch till the `main` branch.

For example let's say we need to back port changes to project `leap` which has two release branches `release/3.1`, 
`release/3.2` and a `main` branch. Here is what we should do:

- Create a branch with the changes

- Create a PR into `release/3.1` from that branch

  - Once approved, merge into `release/3.1`

- Create a branch that merges `release/3.1` into `release/3.2`

- Create a PR into `release/3.2` from that branch

  - Once approved, merge into `release/3.2`

- Create a branch that merges `release/3.2` into main

- Create a PR into `main` from that branch

  - Once approved, merge into `main`
