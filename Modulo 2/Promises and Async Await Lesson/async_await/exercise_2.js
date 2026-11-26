
async function getUser(userId) {
    const url = `https://reqres.in/api/users/${userId}`;

    try {
        const response = await fetch(url);

        if (response.status === 404) {
            throw new Error("User not found");
        }

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const result = await response.json();

        console.log(result.data);

    } catch (error) {
        console.error(error.message);
    }
}

getUser(23);
