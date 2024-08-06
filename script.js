// setInterval(function () {
//     document.title = new Date().toTimeString();
// }, 1000);

const face = document.querySelector(".face");

function createRotationElement(position, content, className) {
    const div = document.createElement("div");
    const fixedRotation = document.createElement("div");
    const degrees = position * 30 % 360;
    fixedRotation.style.transform = `rotate(${-degrees}deg)`;
    fixedRotation.style.width = "min-content";
    fixedRotation.innerHTML = content;
    div.appendChild(fixedRotation);
    div.classList.add(className);
    div.style.transform = `rotate(${degrees}deg)`;
    face.appendChild(div);
}

function createNumbersAndDots() {
    for (let num = 1; num < 13; num++) {
        createRotationElement(num + 3, num, "number");
        createRotationElement(num, "&#x2022;", "dot");
    }
}

function createFace() {
    createNumbersAndDots();
}

createFace();