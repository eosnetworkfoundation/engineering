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

##################################
# build out OpenAPI Docs from yaml
source ${SCRIPT_DIR}/generate_openapi.sh
GenOpenAPI $ROOT_DIR $SCRIPT_DIR
source ${SCRIPT_DIR}/generate_javadoc.sh
GenJavaDoc $ROOT_DIR $SCRIPT_DIR
