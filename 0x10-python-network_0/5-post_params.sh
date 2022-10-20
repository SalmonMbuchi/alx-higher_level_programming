#!/bin/bash
# Send a POST request with an encoded URL
curl -s -X POST "$1"?email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD
