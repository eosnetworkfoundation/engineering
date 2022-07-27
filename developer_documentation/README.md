# Automated Documentation #
Scripts to generate Web Documentation Portal. Goal of this project is create a single documentation portal linking together documentation across the EOS Network's code repositories. This portal will make an effort to make it easy to build and maintain EOS projects.
* Single place EOS documentation
* Unified presentation of documentation
* Single navigation hierarchy covering documentation
* Consistent UI for documentation

In addition, tools are included to help maintain documentation in source repositories. An example is broken link crawlers, looking for bad links in .md files.

## Organization ##

Overview of documentation folder structure:
* devdocs - docusarus
   * eosdocs - toplevel markdown folder
      * client-side - code repositories for developing clients
      * smart-contracts - markdown documentation on contracts, and cdt
      * developer-tools - markdown documentation on nodeos, cleos, and DUNE
* reference - static html root (*sub dirs one-2-one with git repos*)
   * mandel-contracts
   * mandel-cdt
   * ...
   * swiftdocs


### `Coverage` ###

|   Topic  |  Source Repository  | Top Level Path | Delivered By |
|  ------- | ------------------- | -------------- | ------------ |
| Nodeos HTTP API | [mandel](https://github.com/eosnetworkfoundation/mandel) | reference/mandel-plugins | static html with redocly |
| JS and Node Documentation | [mandel-eosjs](https://github.com/eosnetworkfoundation/mandel-eosjs) | eosdocs/client-side/jsdocs | docusaurus |
| Swift Documentation | [mandel-swift](https://github.com/eosnetworkfoundation/mandel-swift) | reference/swiftdocs | static html |
| Java Documenation | [mandel-java](https://github.com/eosnetworkfoundation/mandel-java) | reference/javadocs | static html |
| Smart Contracts | [mandel-contracts](https://github.com/eosnetworkfoundation/mandel-contracts) | reference/mandel-contracts | static html |
| Contract Developer Tools | [mandel.cdt](https://github.com/eosnetworkfoundation/mandel.cdt) | reference/mandel-cdt | static html |
| DUNE -local host | [DUNE](https://github.com/eosnetworkfoundation/DUNE.git) | eosdocs/developer-tools/dune | docusarus |
| Nodeos | [DUNE](https://github.com/eosnetworkfoundation/DUNE.git) | eosdocs/developer-tools/01_nodeos | docusarus |
| Cleos | [DUNE](https://github.com/eosnetworkfoundation/DUNE.git) | eosdocs/developer-tools/02_cleos | docusarus |
| Mandel Install | [DUNE](https://github.com/eosnetworkfoundation/DUNE.git) | eosdocs/developer-tools/00_install | docusarus |

## Initialize Content Repository ##
See [First Install Software](docs/FirstInstallSoftware.md) for all the dependancies.

The initialization script is not destructive, copies in files and creates directories when they do not exist. If they do exist does nothing.
```console
$ cd scripts
$ ./initialize_repository.sh -d /path/to/webroot
```

After running you will find two directories under webroot `devdocs` and `reference`.
* `devdocs` root for docusaurus project
* `reference` static html/js/css served directly by webserver

The `reference` directory will be served by nginx directly. While `devdocs` will be served on a separate port and reversed proxied by nginx. Underneather `devdocs/eosdocs` you will find the documentation. The main index.md file will be located under `/path/to/webroot/devdocs/eosdocs`
```console
$ curl http://host.com/eosdocs/
```

## Generating and Installing Content ##
Clones various git repos, extracts documentation and then copies to webroot folder. The `-u` option switches protocol to http for docs.eosnetwork.com, because https is not supported at this time. Without the `-u` option protocol reverts to https.
```console
$ cd scripts
$ ./run_me_to_gen_docs.sh -u -d /path/to/webroot
```

After running there will be many files under `/path/to/webroot/devdocs/eosdocs` and under `/path/to/webroot/reference`.

## Last Step ##
The doc6s static html is nested under too many directory. Surface the data
<<<<<<< HEAD
<<<<<<< HEAD
=======
```
mv /path/to/webroot/devdocs/eosdocs/build/* /path/to/webroot
rm -rf /path/to/webroot/devdocs
>>>>>>> a3a795d (squash merge to main; generate docs on docs.eosnetwork.com)
```
mv /path/to/webroot/devdocs/eosdocs/build/* /path/to/webroot
rm -rf /path/to/webroot/devdocs
```


=======
```
mv /path/to/webroot/devdocs/eosdocs/build/* /path/to/webroot
rm -rf /path/to/webroot/devdocs
```
>>>>>>> origin/main



See [Generating Documents](docs/GeneratingDocuments.md) for additional details
