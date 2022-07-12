# Automated Documentation #
Scripts to generate Web Documentation Portal. Goal of this project is create a single documentation portal linking together documentation across the EOS Network's code repositories. This portal will make an effort to make it easy to build and maintain EOS projects.
* Single place EOS documentation
* Unified presentation of documentation
* Single navigation heirarchy covering documentation
* Consistent UI for documentation

In addition, tools are included to help maintain documentation in source repositories. An example is broken link crawlers, looking for bad links in .md files.

## Coverage ##

|   Topic  |  Source Repository  |
|  ------- | ------------------- |
| Nodeos HTTP API | [mandel](https://github.com/eosnetworkfoundation/mandel) |
| JS and Node Documentation | [mandel-eosjs](https://github.com/eosnetworkfoundation/mandel-eosjs) |
| Swift Documentation | [mandel-swift](https://github.com/eosnetworkfoundation/mandel-swift) |
| Java Documenation | [mandel-java](https://github.com/eosnetworkfoundation/mandel-java) |
| Smart Contracts | [mandel-contracts](https://github.com/eosnetworkfoundation/mandel-contracts) |
| Developer Tools | [mandel.cdt](https://github.com/eosnetworkfoundation/mandel.cdt) |

## Initialize Content Repository ##
See [First Install Software](docs/FirstInstallSoftware.md) for all the dependancies.

The initialization script is not destructive, copies in files and creates directories when they do not exist. If they do exist does nothing.
```console
$ cd scripts
$ ./initialize_repository.sh -d /path/to/webroot
```

After running you will find a empty index.html file in the `/path/to/webroot/eosdocs`
```console
$ curl http://host.com/eosdocs/
```

## Generating and Installing Content ##
clones various git repos, extracts documentation and then copies to webroot folder
```console
$ cd scripts
$ ./run_me_to_gen_docs.sh -d /path/to/webroot
```

After running there will be many files under `/path/to/webroot/eosdocs`

See [Generating Documents](docs/GeneratingDocuments.md) for additional details
