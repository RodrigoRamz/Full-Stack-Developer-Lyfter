
function getPokemon(pokemonName) {
    const url = `https://pokeapi.co/api/v2/pokemon/${pokemonName}`;

    return fetch(url)
        .then(response => {
            if (response.status === 404) {
                throw new Error(`Pokemon not found: ${pokemonName}`);
            }

            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }

            return response.json();
        });
}

const pokemonPromises = [
    getPokemon("pikachu"),
    getPokemon("charmander"),
    getPokemon("bulbasaur")
];

Promise.any(pokemonPromises)
    .then(pokemon => {
        console.log(pokemon.name);
    })
    .catch(error => {
        console.error(error.message);
    });
