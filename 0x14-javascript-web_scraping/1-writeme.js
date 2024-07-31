#!/usr/bin/node

const fs = require('fs');

const args = process.argv;
const content = args[3];
const filePath = args[2];

fs.writeFile(filePath, content, 'utf8', err => {
  if (err) throw err;
});
