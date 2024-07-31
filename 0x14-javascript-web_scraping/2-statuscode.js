#!/usr/bin/node
const request = require('request');

const args = process.argv;
const url = args[2];

request(url, (error, response, body) => {
  if (error) throw error;
  console.log('code:', response.statusCode);
});
