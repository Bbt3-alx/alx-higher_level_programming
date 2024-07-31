#!/usr/bin/node
const request = require('request');

const args = process.argv;
const movieId = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) throw error;
  const film = JSON.parse(body);
  console.log(film.title);
});
