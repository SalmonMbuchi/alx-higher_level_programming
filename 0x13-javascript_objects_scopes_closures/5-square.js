#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// sub class
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
