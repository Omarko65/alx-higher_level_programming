#!/bin/bash
# a script that sends a header variable to a url
curl -sH 'X-School-User-Id: 98' "$1"
