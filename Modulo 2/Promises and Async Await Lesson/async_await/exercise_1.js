async function getUser(userId) {
    const url = `https://reqres.in/api/users/${userId}`;

    const response = await fetch(url);

    const result = await response.json();

    console.log(result.data);
}

getUser(2);