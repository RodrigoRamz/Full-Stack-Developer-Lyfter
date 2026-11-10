const fs = require("fs");
const path = require("path");


function checkNumber(number, evenCallback, oddCallback) {
    if (!Number.isInteger(number)) {
        console.log("Please enter a valid integer.");
        return;
    }

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
checkNumber(7.5, showEven, showOdd);
checkNumber("8", showEven, showOdd);

const file1Path = path.join(__dirname, "first_file.txt");
const file2Path = path.join(__dirname, "second_file.txt");

fs.readFile(file1Path, "utf8", (error, data1) => {
    if (error) {
        console.log(error);
        return;
    }

    fs.readFile(file2Path, "utf8", (error, data2) => {
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