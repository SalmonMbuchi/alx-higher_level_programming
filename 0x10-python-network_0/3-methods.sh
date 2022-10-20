#!/bin/bash
# Display all HTTP methods the server accepts
curl -s "$1" -X OPTIONS 
