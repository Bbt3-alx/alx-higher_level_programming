#!/usr/bin/node
const request = require('request');
const args = process.argv;
const movieId = args[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) throw error;
  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  function fetchCharacter (url, callback) {
    request(url, (error, response, body) => {
      if (error) throw error;
      const character = JSON.parse(body);
      callback(null, character.name);
    });
  }
  function fetchAllCharacters (urls, index = 0) {
    if (index === urls.length) {
      return;
    }

    fetchCharacter(urls[index], (error, name) => {
      if (error) throw error;
      console.log(name);
      fetchAllCharacters(urls, index + 1);
    });
  }

  fetchAllCharacters(characterUrls);
});
