#!/usr/bin/node

// include process module
const process = require('process');

const args = process.argv;

console.log(args[2] + ' is ' + args[3]);
