#!/bin/bash
# A script that post json file to url with curl
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
