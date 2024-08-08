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
        createRotationElement((num + 3) * 30 % 360, num + 12, "small-number", true);
        createRotationElement(num * 30 % 360, "", "dot", true);
    }
    for (let num = 0; num < 60; num++) {
        if (num % 5 != 0) {
            createRotationElement(num * 6 % 360, "", "line", false);
        }
    }
}

function getTime() {
    const date = new Date();
    return {
        hours: date.getHours(),
        minutes: date.getMinutes(),
        seconds: date.getSeconds(),
        timeString: date.toTimeString(),
    };
}

function animateHands() {
    const hourHand = document.querySelector(".hour");
    const minuteHand = document.querySelector(".minute");
    const secondHand = document.querySelector(".second");
    setInterval(function () {
        const date = getTime();
        const hours = date.hours;
        const minutes = date.minutes;
        const seconds = date.seconds;
        document.title = date.timeString;

        hourHand.style.transform = `rotate(${(hours * 30 + minutes / 2) - 90}deg)`;
        minuteHand.style.transform = `rotate(${(minutes * 6 + seconds / 12) - 90}deg)`;
        secondHand.style.transform = `rotate(${(seconds * 6) - 90}deg)`;
    }, 1000);
}

createFace();
animateHands();