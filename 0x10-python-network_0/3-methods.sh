#!/bin/bash
# a script that returns allowed method from a server will accept
curl -sI "$1" | grep "Allow" | sed 's/^.*: //'
