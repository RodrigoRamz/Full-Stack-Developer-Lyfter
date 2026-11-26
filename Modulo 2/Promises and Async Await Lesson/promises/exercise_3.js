
const completedWords = [];

function getWord(word, delay) {
    return new Promise(resolve => {
        setTimeout(() => {
            completedWords.push(word);
            resolve(word);
        }, delay);
    });
}

const wordPromises = [
    getWord("very", 3000),
    getWord("dogs", 1000),
    getWord("cute", 4000),
    getWord("are", 2000)
];

Promise.all(wordPromises)
    .then(() => {
        const sentence = completedWords.join(" ");

        console.log(
            sentence.charAt(0).toUpperCase() + sentence.slice(1)
        );
    })
    .catch(error => {
        console.error(error.message);
    });
