#!/usr/bin/env bash

###############
# generates swiftdocs
# clones directory then replaces URL paths
# this creates markdown
###############

GenSwiftDoc() {
  if [[ $# -lt 2 ]] ; then
      echo 'NOT ENOUGH ARGS: specify web root,  specify script dir'
      exit 1
  fi

  WEB_ROOT=$1
  # location to write docs
  DEST_DIR="${WEB_ROOT}/eosdocs/swiftdocs"
  # place to clone repo
  WORKING_DIR="${2}/../working"
  # repo
  GIT_URL="https://github.com/eosnetworkfoundation/mandel-swift.git"
  # location of markdown docs inside repo
  DOC_PATH="docs"

  # pull from github
  # create working dir if it does not exist
  [ ! -d $WORKING_DIR ] && mkdir $WORKING_DIR

  # clean out old mandel directory if it exists
  [ -d "${WORKING_DIR}/mandel-swift" ] && rm -rf "${WORKING_DIR}/mandel-swift"
  # enter working directory and clone repo
  cd $WORKING_DIR && git clone $GIT_URL && cd "mandel-swift/${DOC_PATH}"

  # update index with proper server url
  #sed 's/https\:\/\/eosio.github.io\/eosio-swift\//https\:\/\/igeebon.com\/eosdocs\/swiftdocs\//' index.md > tmp.md
  sed 's/https\:\/\/eosio.github.io\/eosio-swift\//\/eosdocs\/swiftdocs\//' index.md > tmp.md
  mv tmp.md index.md

  # copy files in, view framework will convert from Markdown to HTML
  cp -R * $DEST_DIR
}
