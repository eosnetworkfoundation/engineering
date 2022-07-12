# Software Installation #

What to install to setup the documentation generation.
* Software requirements
* Links to instructions on how to install software
* Scripts and Instructions for initial setup of web document content

## Webserver ##
TBD

## Docusaurus ##
TBD

## Software ##
### `Redocly` ###
Used to generate HTML from yaml files

Nothing to install this is done via Javascript loaded from a CDN.

### `javadoc` ###
Used to generate javadocs

Recommended to install the open source version of the JDK. This will provide javadoc on the command line.
[AdoptOpenJDK](https://adoptopenjdk.net/releases.html?variant=openjdk8)

### `node & npm` ###
Used for typescript document generation via typedoc

Instructions on downloading and installing node and npm
[Setup Node and NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

### `doxygen` ###
Used to generate documentation from C++ source code.

[Installing Doxygen](https://www.doxygen.nl/manual/install.html)

## Initialize Content Repository ##

Not destructive, copies in files and creates directories when they do not exist. If they do exist does nothing.
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

See [GeneratingDocuments.md] for additional details
