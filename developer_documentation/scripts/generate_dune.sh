#!/usr/bin/env bash

###############
# generates javascript/typescripts docs
# this creates markdown
###############

GenDuneDoc() {
  if [[ $# -lt 2 ]] ; then
      echo 'NOT ENOUGH ARGS: specify web root,  specify script dir'
      exit 1
  fi

  WEB_ROOT=$1
  # location to write docs
  DEST_DIR="${WEB_ROOT}/devdocs/eosdocs/developer-tools/dune"
  # place to clone repo
  WORKING_DIR="${2}/../working"
  # repo, use personal until pull request accepted
  GIT_URL="https://github.com/eosnetworkfoundation/DUNE.git"
  # location of markdown docs inside repo
  DOC_PATH="docs"

  # pull from github
  # create working dir if it does not exist
  [ ! -d $WORKING_DIR ] && mkdir $WORKING_DIR

  # clean out old mandel directory if it exists
  [ -d "${WORKING_DIR}/DUNE" ] && rm -rf "${WORKING_DIR}/DUNE"
  # enter working directory and clone repo
  cd $WORKING_DIR && git clone $GIT_URL && cd "DUNE"

  mkdir markdown_out
  mv ./README.md markdown_out
  mkdir -p markdown_out/docs/images
  cp docs/images/* markdown_out/docs/images

  # copy files in, view framework will convert from Markdown to HTML
  cp -R markdown_out/* $DEST_DIR
}
