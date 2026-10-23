const example = "This is a string!";
const words = [];
let currentWord = "";

for (let i = 0; i < example.length; i++) {
    const character = example[i];

    if (character === " ") {
        words.push(currentWord);
        currentWord = "";
    } else {
        currentWord += character;
    }
}

// Save the last word
if (currentWord !== "") {
    words.push(currentWord);
}

console.log(words);