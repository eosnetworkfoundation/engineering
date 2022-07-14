#!/usr/bin/env bash

###############
# generates docs on smart contracts from c++ source files
# this creates markdown
###############

GenCDTDoc() {
  if [[ $# -lt 2 ]] ; then
      echo 'NOT ENOUGH ARGS: specify web root,  specify script dir'
      exit 1
  fi

  WEB_ROOT=$1
  # location to write docs
  DEST_DIR="${WEB_ROOT}/devdocs/eosdocs/mandel-cdt"
  # place to clone repo
  SCRIPT_DIR=$2
  WORKING_DIR="${SCRIPT_DIR}/../working"
  # repo, use personal until pull request accepted
  GIT_URL="https://github.com/eosnetworkfoundation/mandel.cdt"
  # location of markdown docs inside repo
  DOC_PATH="docs"

  # pull from github
  # create working dir if it does not exist
  [ ! -d $WORKING_DIR ] && mkdir $WORKING_DIR

  # clean out old mandel directory if it exists
  [ -d "${WORKING_DIR}/mandel.cdt" ] && rm -rf "${WORKING_DIR}/mandel.cdt"
  # enter working directory and clone repo
  cd $WORKING_DIR && git clone $GIT_URL && cd "mandel.cdt"
  # copy in doxygen config file
  cp ${SCRIPT_DIR}/mandle.cdt-doxyfile Doxyfile
  # copy in logo
  cp ${SCRIPT_DIR}/../web/eosn_logo.png $DOC_PATH
  # run doxygen
  doxygen

  # copy files in, view framework will convert from Markdown to HTML
  cp -R doxygen_out/html/* $DEST_DIR
}

GenSmartContractDoc() {
  if [[ $# -lt 2 ]] ; then
      echo 'NOT ENOUGH ARGS: specify web root,  specify script dir'
      exit 1
  fi

  WEB_ROOT=$1
  # location to write docs
  DEST_DIR="${WEB_ROOT}/reference/mandel-contracts"
  # place to clone repo
  SCRIPT_DIR=$2
  WORKING_DIR="${SCRIPT_DIR}/../working"
  # repo, use personal until pull request accepted
  GIT_URL="https://github.com/eosnetworkfoundation/mandel-contracts"
  # location of markdown docs inside repo
  DOC_PATH="docs"

  # pull from github
  # create working dir if it does not exist
  [ ! -d $WORKING_DIR ] && mkdir $WORKING_DIR

  # clean out old mandel directory if it exists
  [ -d "${WORKING_DIR}/mandel-contracts" ] && rm -rf "${WORKING_DIR}/mandel-contracts"
  # enter working directory and clone repo
  cd $WORKING_DIR && git clone $GIT_URL && cd "mandel-contracts"
  # copy in doxygen config file
  cp ${SCRIPT_DIR}/mandel-contracts-doxyfile Doxyfile
  # copy in logo
  cp ${SCRIPT_DIR}/../web/eosn_logo.png $DOC_PATH
  # run doxygen
  doxygen

  # copy files in, view framework will convert from Markdown to HTML
  cp -R doxygen_out/html/* $DEST_DIR
}
