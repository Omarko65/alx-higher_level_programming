#!/bin/bash
# a script that displays all http method allowed
curl -sI "$1" | grep 'Allow:' | sed 's/^.*: //'
