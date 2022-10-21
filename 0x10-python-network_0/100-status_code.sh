#!/bin/bash
# Display only the status code
curl -I -s -w "%{http_code}\n" -o /dev/null "$1"
