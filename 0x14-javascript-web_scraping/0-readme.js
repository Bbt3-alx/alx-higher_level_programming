#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const content = args[2];
fs.readFile(content, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
