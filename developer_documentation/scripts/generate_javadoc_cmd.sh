#!/usr/bin/env bash

###############
# generates javadocs on the command line
# greps out package names
# then runs javadoc
# files stored in local directory
# for reference on javadoc http://www.manpagez.com/man/1/javadoc/
###############

if [[ $# -eq 0 ]] ; then
    echo 'NOT ENOUGH ARGS: specify directory of java repository'
    exit 1
fi

SRC_DIR=$1
DEST_DIR="test"
echo "Working on Directory ${SRC_DIR}"

# grep out packages
# first cut: split out the code with the package name
# second cut: remove the trailing ';'
# sort: dedup
PACKAGES=$(grep -Ri '^package' ${SRC_DIR}/* | cut -d: -f 2 | cut -d';' -f1 | sort -u )
# remove package name at begining
PACKAGES=${PACKAGES//package /}
# translate ending newlines to spaces
PACKAGES=${PACKAGES//[$'\t\r\n']/ }

CMD="javadoc -sourcepath ${SRC_DIR} -d ${DEST_DIR} ${PACKAGES}"
echo "running ${CMD}"
javadoc -sourcepath ${SRC_DIR} -d ${DEST_DIR} ${PACKAGES}
