const face = document.querySelector(".face");

function createRotationElement(degrees, content, className, rotate) {
    const div = document.createElement("div");
    const fixedRotation = document.createElement("div");
    fixedRotation.style.transform = `rotate(${rotate ? -degrees : 90}deg)`;
    fixedRotation.innerHTML = content;
    div.appendChild(fixedRotation);
    div.classList.add(className);
    div.style.transform = `rotate(${degrees}deg)`;
    face.appendChild(div);
}

function createFace() {
    for (let num = 1; num < 13; num++) {
        createRotationElement((num + 3) * 30 % 360, num, "number", true);
        createRotationElement(num * 30 % 360, "", "dot", true);
    }
    for (let num = 0; num < 60; num++) {
        if (num % 5 != 0) {
            createRotationElement(num * 6 % 360, "", "line", false);
        }
    }
}

function animateHands() {
    setInterval(function () {
        document.title = new Date().toTimeString();
        
    }, 1000);
}

createFace();