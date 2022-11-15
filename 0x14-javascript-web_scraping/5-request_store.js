#!/usr/bin/node
// Gets the content of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
request(url).pipe(fs.createWriteStream(file));
