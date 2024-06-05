#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.characters.forEach(async function (element) {
      await new Promise((resolve, reject) => {
        request(element, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    });
  }
});
