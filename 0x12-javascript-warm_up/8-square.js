#!/usr/bin/node
// prints a square
const process = require('process');

const args = process.argv;

if (args.length < 3 || !parseInt(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    let row = '';
    for (let j = 0; j < args[2]; j++) {
      row += 'X';
    }
    console.log(row + ' ');
  }
}
