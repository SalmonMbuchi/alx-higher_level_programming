#!/bin/bash
# Display all HTTP methods the server accepts
curl -is -X OPTIONS "$1" | grep -Pio 'Allow:\s\K.*' 
