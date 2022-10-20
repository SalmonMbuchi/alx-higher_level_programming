#!/bin/bash
# Send a GET request with a parameter and its value
curl -s -X GET -d 'X-School-User-Id=98' "$1"
