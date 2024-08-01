#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
const characterId = '18';
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

let nbMovie = 0;
request(url, (error, response, body) => {
  if (error) throw error;
  const films = JSON.parse(body).results;

  films.forEach(film => {
    if (film:x.characters.includes(characterUrl)) {
      nbMovie++;
    }
  });

  console.log(nbMovie);
});
