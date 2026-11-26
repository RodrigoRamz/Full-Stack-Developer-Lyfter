
function getUser(userId) {
    const url = `https://reqres.in/api/users/${userId}`;

    return fetch(url)
        .then(response => {
            if (response.status === 404) {
                throw new Error("User not found");
            }

            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }

            return response.json();
        })
        .then(result => {
            console.log(result.data);
        })
        .catch(error => {
            console.error(error.message);
        })
        .finally(() => {
            console.log("Request completed");
        });
}

getUser(2).then(() => getUser(23));
