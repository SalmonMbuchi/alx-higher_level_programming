#!/usr/bin/node
// prints the no. of arguments already printed and the new arfument value
let count = 0;
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
