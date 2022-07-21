# Generating Documents #
How to guide on generating the documents or regenerating

## Static Index Files ##

There are 4 static index files copied from the `engineering` repo.

* developer_documentation/web/index.md -> /eosdocs/index.md
* developer_documentation/web/api-listing.md -> /eosdocs/api-listing.md
* developer_documentation/web/reference-index.html -> /reference/index.html
* developer_documentation/web/client-side/index.md -> /eosdocs/client-side/index.md

## Mandel Open APIs ##
These are the HTTP API documented in YAML files, and they are stored in the mandel github repository. Redocly HTML files are setup to read directly from the YAML files and parse them via javascript code loaded off a CDN. Specifically [Redocly](https://redocly.com/docs/redoc/quickstart/) is used.

These are not markdown files so you will find them under `reference/mandel-plugins/`

## Nodeos Cloes and Kloes ##
The markdown is pulled from github under the `mandel` repo. A script is run to add meta-data to the document for better viewing.

These are markdown file found under `eosdocs/developer-tools/`

## Mandel JavaDocs ##
The repo `mandel-java` is cloned and javadocs command is run to generate the docs.

These are not markdown files so you will find them under `reference/javadocs/`

## Mandel Swift ##
The repo `mandel-swift` is cloned and the pre-generated swiftdocs and the source code are copied into the specified directory.

These are not markdown files so you will find them under `reference/swiftdocs/`

There is one markdown file, an index of the top level interfaces in Swift. This markdown is copied from github, and it lives under `eosdocs/client-side/swiftdocs`

## Mandel Typescript ##
The repo `mandel-eosjs` is cloned and typedoc runs to generate the documentation.

Typedoc outputs as markdown, and all files are located under `eosdocs/client-side/jsdocs`

## Mandel Contract Reference ##
The `mandel-contracts` is cloned and doxygen is run to generate html files.

These are not markdown files so they are stored under `reference/mandel-contracts`

## Mandel Contract Developer Toolkit ##
The `mandel.cdt` is cloned and doxygen is run to generate html files.

These are not markdown files so they are stored under `reference/mandel.cdt`

# Setting up New Locales #
**Docusaurus i18n configs**
If it is your first time run the write-translation plugin to generate the i18n files. Look at *root/i18n* for these files. These file support all of your theme stuff including navbar. Look at *root/i18n/xx* and start translating the expressions. These translations will be picked up by Docusaurus
```
npm run write-translations -- --locale en
```

## Updating Content ##
When changing content under the `engineering/developer_documentation/web` folder make sure to check for localized versions. You will find those versions under `i18n/xx/docusaurus-plugin-content-docs/current`. For example when you change `api-listing.md` you must also change `i18n/zh/docusaurus-plugin-content-docs/current/api-listing.md` and change `i18n/ko/docusaurus-plugin-content-docs/current/api-listing.md`.
