#!/usr/bin/node
const request = require('request');
const args = process.argv;
const apiUrl = args[2];

request(apiUrl, (error, response, body) => {
  if (error) throw error;
  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 0;
      }
      completedTasksByUser[task.userId]++;
    }
  });
  console.log(completedTasksByUser);
});
