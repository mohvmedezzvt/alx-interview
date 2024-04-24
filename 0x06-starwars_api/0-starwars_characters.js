#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];

process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';

request(`https://swapi.dev/api/films/${filmId}`, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Status Code:', response.statusCode);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
