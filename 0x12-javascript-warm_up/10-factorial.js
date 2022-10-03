#!/usr/bin/node
// compute the factorial
const process = require('process');
const args = process.argv;

function factorial (a) {
  if (!a || a <= 1) {
    return 1;
  }
  return (a * factorial(a - 1));
}
console.log(factorial(args[2]));
