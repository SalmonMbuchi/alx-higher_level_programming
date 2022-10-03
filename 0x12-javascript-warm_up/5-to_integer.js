#!/usr/bin/node
// convert first argument to an integer
const process = require('process');

const args = process.argv;

if (!parseInt(args[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
