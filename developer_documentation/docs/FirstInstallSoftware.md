# Software Installation #

What to install to setup the documentation generation.
* Software requirements
* Links to instructions on how to install software
* Scripts and Instructions for initial setup of web document content

## Webserver ##
TBD

## Docusaurus ##
This is installed by the `initialize_repository.sh` script. The script runs this installation because the docusarus install creates a directy structure. 

## Software ##
### `Redocly` ###
Used to generate HTML from yaml files

Nothing to install this is done via Javascript loaded from a CDN.

### `javadoc` ###
Used to generate javadocs

Recommended to install the open source version of the JDK. This will provide javadoc on the command line.
[AdoptOpenJDK](https://adoptopenjdk.net/releases.html?variant=openjdk8)

### `node & npm` ###
Used to general markdown from typescript documentation or openapi

Instructions on downloading and installing node and npm
[Setup Node and NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

### `doxygen` ###
Used to generate documentation from C++ source code.

[Installing Doxygen](https://www.doxygen.nl/manual/install.html)
