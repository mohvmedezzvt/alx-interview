#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
const request = require('request');
const filmId = process.argv[2];

const getCharacters = new Promise((resolve, reject) => {
  request.get(
        `https://swapi-api.alx-tools.com/api/films/${filmId}/`,
        (error, response, body) => {
          if (!error) {
            try {
              resolve(JSON.parse(body).characters);
            } catch (error) {
              reject(error);
            }
          }
          reject(error);
        }
  );
});

getCharacters.then((characters) => {
  const charchtersPromises = [];

  for (const character of characters) {
    charchtersPromises.push(
      new Promise((resolve, reject) => {
        request.get(character, (error, response, body) => {
          if (!error) {
            try {
              resolve(JSON.parse(body).name);
            } catch (error) {
              reject(error);
            }
          }
          reject(error);
        });
      })
    );
  }

  Promise.all(charchtersPromises).then((names) => {
    names.forEach((name) => console.log(name));
  });
});
