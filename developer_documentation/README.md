# Automated Documentation #
Scripts to generate Web Documentation Portal. Goal of this project is create a single documentation portal linking together documentation across the EOS Network's code repositories. This portal will make an effort to make it easy to build and maintain EOS projects.
* Single place EOS documentation
* Unified presentation of documentation
* Single navigation heirarchy covering documentation
* Consistent UI for documentation

In addition, tools are included to help maintain documentation in source repositories. An example is broken link crawlers, looking for bad links in .md files.

## Coverage ##

|   Topic  |  Source Repository  | Top Level Path | Delivered By |
|  ------- | ------------------- | -------------- | ------------ |
| Nodeos HTTP API | [mandel](https://github.com/eosnetworkfoundation/mandel) | eosdocs/mandel-plugins | docusaurus |
| JS and Node Documentation | [mandel-eosjs](https://github.com/eosnetworkfoundation/mandel-eosjs) | eosdocs/jsdocs | docusaurus |
| Swift Documentation | [mandel-swift](https://github.com/eosnetworkfoundation/mandel-swift) | reference/swiftdocs | static html |
| Java Documenation | [mandel-java](https://github.com/eosnetworkfoundation/mandel-java) | reference/javadocs | static html |
| Smart Contracts | [mandel-contracts](https://github.com/eosnetworkfoundation/mandel-contracts) | eosdocs/mandel-contracts | docusarus |
| Developer Tools | [mandel.cdt](https://github.com/eosnetworkfoundation/mandel.cdt) | eosdocs/mandel-cdt/ | docusarus |

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
clones various git repos, extracts documentation and then copies to webroot folder
```console
$ cd scripts
$ ./run_me_to_gen_docs.sh -d /path/to/webroot
```

After running there will be many files under `/path/to/webroot/devdocs/eosdocs`.

## Running Docusaurus ##
Your `/path/to/webroot/devdocs` and your port may differ
```console
$ cd /path/to/webroot/devdocs
$ npm run serve -- --port 39999
```

See [Generating Documents](docs/GeneratingDocuments.md) for additional details
