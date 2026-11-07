const paragraph = document.getElementById("text");
const button = document.getElementById("color-button");
const colors = ["red", "blue", "green", "yellow", "cyan", "pink"];

function changeColor() {
    const randomIndex = Math.floor(Math.random() * colors.length);
    paragraph.style.backgroundColor = colors[randomIndex];
}

button.addEventListener("click", changeColor);