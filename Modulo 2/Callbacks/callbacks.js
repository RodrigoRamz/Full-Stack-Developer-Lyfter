function checkNumber(number, evenCallback, oddCallback) {
    if (number % 2 === 0) {
        evenCallback();
    } else {
        oddCallback();
    }
}

function showEven() {
    console.log("The number is even!");
}

function showOdd() {
    console.log("The number is odd!");
}

checkNumber(10, showEven, showOdd);
checkNumber(7, showEven, showOdd);

const fs = require("fs");

fs.readFile("first_file.txt", "utf8", (error, data1) => {
    if (error) {
        console.log(error);
        return;
    }

    fs.readFile("second_file.txt", "utf8", (error, data2) => {
        if (error) {
            console.log(error);
            return;
        }

        const words1 = data1.trim().split(/\r?\n/);
        const words2 = data2.trim().split(/\r?\n/);

        const repeatedWords = words1.filter((word) => {
            return words2.includes(word);
});

        console.log(repeatedWords.join(" "));
        
    });
});