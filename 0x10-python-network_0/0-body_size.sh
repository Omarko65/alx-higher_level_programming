#!/bin/bash
# a script that displays size of http body response
curl -si "$1" | grep 'content-length' | tr dc '0-9'
