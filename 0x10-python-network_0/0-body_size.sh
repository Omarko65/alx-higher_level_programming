#!/bin/bash
# a script that returns size in bytes of body of a url
curl -si "$1" | grep 'Content-Length' | tr -dc '0-9'
