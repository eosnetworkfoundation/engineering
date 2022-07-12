#!/usr/bin/env bash

# This script is not destructive. It initialized web documentation.
# It creates diretory structure when dirs do not exist
# It copies over a few static web files (html, css, js)
# created July 2022
# author @ericpassmore

########
# FUNCTIONS
Help() {
  echo "Creates directories and installs inital templates"
  echo "  Not destructive will only create if items do not exist"
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

echo "creating directories and adding templates under ${ROOT_DIR}"

# make directories
[ ! -d "${ROOT_DIR}/eosdocs" ] && mkdir "${ROOT_DIR}/eosdocs"
[ ! -d "${ROOT_DIR}/eosdocs/openapi" ] && mkdir "${ROOT_DIR}/eosdocs/openapi"
[ ! -d "${ROOT_DIR}/eosdocs/openapi/mandel-plugins" ] && mkdir "${ROOT_DIR}/eosdocs/openapi/mandel-plugins"
[ ! -d "${ROOT_DIR}/eosdocs/mandel-plugins" ] && mkdir "${ROOT_DIR}/eosdocs/mandel-plugins"
[ ! -d "${ROOT_DIR}/eosdocs/mandel-contracts" ] && mkdir "${ROOT_DIR}/eosdocs/mandel-contracts"
[ ! -d "${ROOT_DIR}/eosdocs/javadocs" ] && mkdir "${ROOT_DIR}/eosdocs/javadocs"
[ ! -d "${ROOT_DIR}/eosdocs/jsdocs" ] && mkdir "${ROOT_DIR}/eosdocs/jsdocs"
[ ! -d "${ROOT_DIR}/eosdocs/swiftdocs" ] && mkdir "${ROOT_DIR}/eosdocs/swiftdocs"

echo "copying in static files, will not overwrite existing files"

# copy over the main index file
[ ! -f "${ROOT_DIR}/eosdocs/index.html" ] && cp "${SCRIPT_DIR}/../web/index.html" "${ROOT_DIR}/eosdocs/index.html"
# copy over the html with openapi documentation from mandel
for i in ${SCRIPT_DIR}/../web/mandel-plugins/*.html
do
  file_name=$(basename ${i})
  [ ! -f "${ROOT_DIR}/eosdocs/mandel-plugins/${file_name}" ] && cp $i "${ROOT_DIR}/eosdocs/mandel-plugins/${file_name}"
done
