#!/bin/bash
# a script that displays all http method allowed
curl -i "$1" | grep 'Allow:' | sed 's/^.*: //'
