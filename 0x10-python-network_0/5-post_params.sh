#!/bin/bash
# Send a POST request with an encoded URL
curl -sX POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
