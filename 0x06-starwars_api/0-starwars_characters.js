#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

/**
 * Fetches the name of a character given the URL to their data.
 * @param {string} characterUrl - The URL to the character data.
 * @returns {Promise<string>} - A promise that resolves to the character's name.
 */
function fetchCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(
          new Error(
            `Error fetching character ${characterUrl}: ${error.message}`
          )
        );
      } else {
        try {
          const characterName = JSON.parse(body).name;
          resolve(characterName);
        } catch (parseError) {
          reject(
            new Error(
              `Error parsing character data from ${characterUrl}: ${parseError.message}`
            )
          );
        }
      }
    });
  });
}

/**
 * Fetches the details of a film and logs the names of all characters in that film.
 */
async function fetchFilmCharacters () {
  request(url, async (error, response, body) => {
    if (error) {
      console.error(`Error fetching film: ${error.message}`);
    } else {
      try {
        const data = JSON.parse(body);

        // Check if the film was found
        if (data.detail === 'Not found') {
          console.error('Film not found. Please provide a valid film ID.');
          return;
        }

        const characters = data.characters;

        if (!Array.isArray(characters)) {
          throw new Error('characters is not an array');
        }

        for (const characterUrl of characters) {
          try {
            const characterName = await fetchCharacterName(characterUrl);
            console.log(characterName);
          } catch (err) {
            console.error(err);
          }
        }
      } catch (parseError) {
        console.error(`Error parsing film data: ${parseError.message}`);
      }
    }
  });
}

// Execute the function to fetch and log film characters
fetchFilmCharacters();
