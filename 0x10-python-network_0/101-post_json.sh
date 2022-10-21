#!/bin/bash
# Send a JSON POST request
curl -X POST "$1" -H 'Content-Type: application/json' --data @"$2"
