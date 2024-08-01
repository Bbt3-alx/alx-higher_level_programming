#!/usr/bin/node
const request = require('request');
const args = process.argv;
const movieId = args[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) throw error;
  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  characterUrls.forEach(url => {
    request(url, (error, reponse, body) => {
      if (error) throw error;
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
