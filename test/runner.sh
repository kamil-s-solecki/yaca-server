#!/bin/bash


function run() {
    CLR='\033[1;36m'
    NC='\033[0m' # No Color

    echo ""
    echo -e "${CLR}=========================================================="
    echo -e "${CLR}    >>> Running $1 <<<"
    echo -e "${CLR}==========================================================${NC}"
    echo ""
    python $1
}

export -f run

find . -iname '*_test.py' -exec bash -c 'run {}' \;
