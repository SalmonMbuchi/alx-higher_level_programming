#!/usr/bin/node
// Compute the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  const tasks = JSON.parse(body);
  const completed = {};
  tasks.forEach((task) => {
    if (task.completed && completed[task.userId] === undefined) {
      completed[task.userId] = 1;
    } else if (task.completed) {
      completed[task.userId] += 1;
    }
  });
  console.log(completed);
});
