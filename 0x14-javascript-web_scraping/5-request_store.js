#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const filePath = args[3];

request(url, (error, response, body) => {
  if (error) throw error;
  fs.writeFile(filePath, body, 'utf8', err => {
    if (err) throw err;
  });
});
