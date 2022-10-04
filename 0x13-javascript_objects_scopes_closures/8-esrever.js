#!/usr/bin/node
// returns the reversed version of a list
exports.esrever = function (list) {
  const reverse = [];
  const len = list.length - 1;
  for (let i = len; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};
