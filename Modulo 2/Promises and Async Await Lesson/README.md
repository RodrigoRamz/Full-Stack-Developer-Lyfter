# Promises and Async/Await Lesson

## Overview

This project demonstrates asynchronous programming in JavaScript using Promises, Async/Await, the Fetch API, and DOM manipulation.

## Technologies

- JavaScript (ES6+)
- Node.js
- HTML5
- CSS3
- Fetch API
- ReqRes API
- PokeAPI

## Async/Await Exercises

| Exercise | Description |
|---|---|
| Exercise 1 | Retrieve user information from ReqRes using Async/Await. |
| Exercise 2 | Handle HTTP errors and display an appropriate message when a user is not found. |
| Exercise 3 | Build an interactive web application to search for users by ID and display their information. |

## Promises Exercises

| Exercise | Description |
|---|---|
| Exercise 1 | Retrieve information about three Pokémon concurrently using Promise.all(). |
| Exercise 2 | Retrieve the first successfully fulfilled Pokémon request using Promise.any(). |
| Exercise 3 | Combine setTimeout() and Promise.all() to generate a sentence based on the completion order of asynchronous operations. |
| Exercise 4 | Retrieve user information and handle errors using then(), catch(), and finally(). |

## How to Run

Run the JavaScript exercises from the lesson directory:

- `node async_await/exercise_1.js`
- `node async_await/exercise_2.js`
- `node promises/exercise_1.js`
- `node promises/exercise_2.js`
- `node promises/exercise_3.js`
- `node promises/exercise_4.js`

To run the web application:

1. Navigate to `async_await/exercise_3`.
2. Run `python3 -m http.server 8000`.
3. Open `http://localhost:8000` in a web browser.

## Implementation Highlights

- HTTP response validation.
- Error handling for unsuccessful API requests.
- Concurrent asynchronous operations.
- User input validation.
- Dynamic DOM manipulation using textContent.
- Prevention of repeated submissions during active requests.
- Separation of HTML, CSS, and JavaScript responsibilities.

## External APIs

- ReqRes: https://reqres.in/
- PokeAPI: https://pokeapi.co/

An active internet connection is required to execute exercises that consume external APIs.