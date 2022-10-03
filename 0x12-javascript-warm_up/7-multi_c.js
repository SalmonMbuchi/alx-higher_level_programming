#!/usr/bin/node
// prints x times "C is fun"

// import the module
const process = require('process');

const args = process.argv;

if (args.length <= 2 || !parseInt(args[2])) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
}
