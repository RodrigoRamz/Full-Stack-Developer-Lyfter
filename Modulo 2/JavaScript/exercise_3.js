const temperatures = [0, 10, 20, 30, 40];

// Convert Celsius temperatures to Fahrenheit
const fahrenheit = temperatures.map(temp => temp * 9 / 5 + 32);

// Print the converted temperatures
console.log(fahrenheit);