#!/usr/bin/env bash

#GenOpenAPI /path/to/web /path/to/script

# clones the mandel repo and copies yaml files into web root dir
GenOpenAPI() {
  if [[ $# -lt 2 ]] ; then
      echo 'NOT ENOUGH ARGS: specify web root,  specify script dir '
      exit 1
  fi
  WEB_ROOT=$1
  WORKING_DIR="${2}/../working"
  GIT_URL="https://github.com/eosnetworkfoundation/mandel"

  # pull from github
  # create working dir if it does not exist
  [ ! -d $WORKING_DIR ] && mkdir $WORKING_DIR

  # clean out old mandel directory if it exists
  [ -d "${WORKING_DIR}/mandel" ] && rm -rf "${WORKING_DIR}/mandel"
  # enter working directory and clone repo
  cd $WORKING_DIR && git clone $GIT_URL


  # this copy is destructive
  for i in $(find mandel -name "*.yaml")
  do
    cp $i "${WEB_ROOT}/eosdocs/openapi/mandel-plugins/"
  done
}
