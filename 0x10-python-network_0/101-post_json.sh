#!/bin/bash
# a script that sends a json POST request to a URL
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
