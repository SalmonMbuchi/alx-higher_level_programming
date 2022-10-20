#!/bin/bash
# Display 200 status code response
curl -s -o /dev/null -w http_code "$1"
