#!/bin/bash
# A script that post json file to url with curl
curl -X "$1" -d @"$2"
