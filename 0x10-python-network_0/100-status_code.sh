#!/bin/bash
# a script that gets status code of response header
curl -s -o response.txt -w "%{http_code}" "$1"
