#!/usr/bin/node
// Display the status code of a GET request

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
request(url + id, (error, response, body) => {
  if (error) console.log(error);

  console.log(JSON.parse(body).title);
});
