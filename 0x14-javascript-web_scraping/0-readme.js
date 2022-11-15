#!/usr/bin/node
// Read and print the contents of a file

const fs = require('fs');

const filename = process.argv[2];
fs.readFile(filename, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
