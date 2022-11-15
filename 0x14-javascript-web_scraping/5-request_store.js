#!/usr/bin/node
// Gets the content of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
request(url, (error, response, body) => {
  if (error) console.log(error);
  const content = JSON.parse(JSON.stringify(body.trim()));
  fs.writeFile(file, content, (err) => {
    if (err) console.log(err);
  });
});
