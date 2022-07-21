#!/usr/bin/env bash

# This script will overwrite existing files
# Creates the documentation in the specified web root direction
# created July 2022
# author @ericpassmore

########
# FUNCTIONS
Help() {
  echo "Creates web version of documentation pulling together documentation from several gitrepositories across the EOS Networks"
  echo ""
  echo "Syntax: initialize_repository [-h|d]"
  echo "options:"
  echo "-h: print this help"
  echo "-d: specificy web root directory and destination"
  exit 1
}

########
# Get the options
while getopts "hd:" option; do
   case $option in
      h) # display Help
         Help
         ;;
      d) # set dir
        ROOT_DIR=${OPTARG}
        ;;
      :) # no args
        echo "missing '-d' directory, '-h' for help"; exit 1;
        ;;
      *) # abnormal args
        echo "unexpected arguments, '-h' for help"; exit 1;
        ;;
   esac
done

######
# main
# check for parameters
if [ -z $ROOT_DIR ]; then
  echo "missing '-d' directory, '-h' for help"; exit 1;
fi
# compute script dir for copying files from here to web directory
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# HTML Header File
HEADER_HTML_FILE="${SCRIPT_DIR}/../web/header.html"
# MAIN Index page
cp ${SCRIPT_DIR}/../web/index.md "${ROOT_DIR}/devdocs/eosdocs"
# Client Index Page
cp ${SCRIPT_DIR}/../web/client-side/index.md "${ROOT_DIR}/devdocs/eosdocs/client-side/"
# Overwrite docusarus config
cp "${SCRIPT_DIR}/../config/docusaurus.config.js" "${ROOT_DIR}/devdocs"
# Overwrite entry page for docusarus
cp "${SCRIPT_DIR}/../web/docusaurus/index.tsx" "${ROOT_DIR}/devdocs/src/pages"

##################################
# build out OpenAPI Docs from yaml
source ${SCRIPT_DIR}/generate_mandeldocs.sh
GenOpenAPI $ROOT_DIR $SCRIPT_DIR
GenMandelToolDoc $ROOT_DIR $SCRIPT_DIR
# build out javadocs
source ${SCRIPT_DIR}/generate_javadoc.sh
GenJavaDoc $ROOT_DIR $SCRIPT_DIR
# move over markdown for swift
source ${SCRIPT_DIR}/generate_swiftdoc.sh
GenSwiftDoc $ROOT_DIR $SCRIPT_DIR
# use typedoc to generate JS documenation in markdown
source ${SCRIPT_DIR}/generate_jsdoc.sh
GenJSDoc $ROOT_DIR $SCRIPT_DIR
# build out smart contract documenation using doxygen
source ${SCRIPT_DIR}/generate_smartcontractdoc.sh
GenSmartContractDoc $ROOT_DIR $SCRIPT_DIR
GenCDTDoc $ROOT_DIR $SCRIPT_DIR
# build Dune docs
#source ${SCRIPT_DIR}/generate_dune.sh
#GenDuneDoc $ROOT_DIR $SCRIPT_DIR

find ${ROOT_DIR}/devdocs/eosdocs/developer-tools -type f | xargs -I{} ${SCRIPT_DIR}/add_title.py {}
find ${ROOT_DIR}/devdocs/eosdocs/client-side -type f | xargs -I{} ${SCRIPT_DIR}/add_title.py {}

cp -r ${SCRIPT_DIR}/../web/docusaurus/i18n ${ROOT_DIR}/devdocs/

echo "NEXT STEPS *******"
cd ${ROOT_DIR}/devdocs
yarn build
