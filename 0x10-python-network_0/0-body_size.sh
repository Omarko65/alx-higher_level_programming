#!/bin/bash
# a script that displays size of http body response
curl -si "$1" | grep 'Content-Length' | tr dc '0-9'
