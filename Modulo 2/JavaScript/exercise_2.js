const numbers = [3, 8, 12, 5, 7, 10, 15, 20];
const evenNumbers = [];

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
        evenNumbers.push(numbers[i]);
    }
}

console.log(evenNumbers);

// Solution 2: Using filter()
const evenNumbersFilter = numbers.filter(number => number % 2 === 0);

console.log("Even numbers using filter:", evenNumbersFilter);