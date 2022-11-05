#!/bin/bash
# sends GET request to a URL and returns rsesponse code
curl -s -o /dev/null -w "%{http_code}" "$1"
