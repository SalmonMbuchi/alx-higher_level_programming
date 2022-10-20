#!/bin/bash
# Display the size of the response message
curl -Is "$1" | grep -Pio 'Content-Length:\s\K([^ ]*)'
