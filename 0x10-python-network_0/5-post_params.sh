#!/bin/bash
# a script that sends a post request a URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
