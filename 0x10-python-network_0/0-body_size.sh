#!/bin/bash
# Display the size of the response message
curl -s http://"$2" | grep Content-Length
