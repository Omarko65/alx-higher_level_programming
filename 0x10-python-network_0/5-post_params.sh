#!/bin/bash
# a script that post parameters to a url
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
