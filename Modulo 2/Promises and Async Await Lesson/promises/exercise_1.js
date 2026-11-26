
function getPokemon(pokemonName) {
    const url = `https://pokeapi.co/api/v2/pokemon/${pokemonName}`;

    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Pokemon not found: ${pokemonName}`);
            }

            return response.json();
        });
}

const pokemonPromises = [
    getPokemon("pikachu"),
    getPokemon("charmander"),
    getPokemon("bulbasaur")
];

Promise.all(pokemonPromises)
    .then(pokemons => {
        pokemons.forEach(pokemon => {
            console.log(pokemon.name);
        });
    })
    .catch(error => {
        console.error(error.message);
    });
