#!/bin/bash
# a script that causes server to respond with message
curl -sX PUT -L -d "user-id=98" -H "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
