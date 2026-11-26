
const userIdInput = document.getElementById("user-id");
const searchButton = document.getElementById("search-button");
const resultContainer = document.getElementById("result");

async function getUser() {
    const userId = Number(userIdInput.value);

    resultContainer.textContent = "";

    if (!Number.isInteger(userId) || userId <= 0) {
        resultContainer.textContent = "Please enter a valid user ID.";
        return;
    }

    const url = `https://reqres.in/api/users/${userId}`;

    searchButton.disabled = true;
    resultContainer.textContent = "Loading...";

    try {
        const response = await fetch(url);

        if (response.status === 404) {
            throw new Error("User not found");
        }

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const result = await response.json();
        const user = result.data;

        resultContainer.textContent = "";

        const firstName = document.createElement("p");
        firstName.textContent = `First name: ${user.first_name}`;

        const lastName = document.createElement("p");
        lastName.textContent = `Last name: ${user.last_name}`;

        const email = document.createElement("p");
        email.textContent = `Email: ${user.email}`;

        resultContainer.append(firstName, lastName, email);

    } catch (error) {
        resultContainer.textContent = error.message;

    } finally {
        searchButton.disabled = false;
    }
}

searchButton.addEventListener("click", getUser);
