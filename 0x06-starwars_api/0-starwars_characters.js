#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.name);
  }
});
