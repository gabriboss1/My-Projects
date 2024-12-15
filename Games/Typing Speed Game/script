const textOutput = document.getElementById("text-output");
const textInput = document.getElementById("text-input");
const timerDisplay = document.getElementById("timer");
const wpmDisplay = document.getElementById("wpm");
const endScreen = document.getElementById("end-screen");
const endWpm = document.getElementById("end-wpm");
const startBtn = document.getElementById("start-btn");
const redoBtn = document.getElementById("redo-btn");

// Options
const timeSelect = document.getElementById("time-select");
const punctuationToggle = document.getElementById("punctuation-toggle");
const uppercaseToggle = document.getElementById("uppercase-toggle");

let sampleText =
    "order first give we could feel over place between after then write not great increase turn back hold tell";
let words = [];
let currentWordIndex = 0;
let currentInput = "";
let timeLimit = 30; // Default 30s
let timerInterval = null;
let startTime = null;

startBtn.addEventListener("click", startTest);
redoBtn.addEventListener("click", resetTest);

function generateText() {
    let text = sampleText;
    if (punctuationToggle.checked) text += ",.!?";
    if (uppercaseToggle.checked) text = text.replace(/\b\w/g, (c) => c.toUpperCase());

    words = text.split(" ").slice(0, 100); // Limit words
}

function renderText() {
    textOutput.innerHTML = words
        .map((word, index) => {
            let classes = "";
            if (index < currentWordIndex) classes = "correct";
            else if (index === currentWordIndex) classes = "current";
            return `<span class="${classes}">${word}</span>`;
        })
        .join(" ");
    addCursor();
}

function addCursor() {
    const currentWord = document.querySelector(".current");
    currentWord.innerHTML = [...words[currentWordIndex]]
        .map((char, i) => {
            const cursor = i === currentInput.length ? `<span class="text-cursor"></span>` : "";
            return `${char}${cursor}`;
        })
        .join("");
}

function startTest() {
    resetTest();
    generateText();
    renderText();

    textInput.style.display = "block";
    startBtn.style.display = "none";
    document.getElementById("stats").style.display = "flex";

    textInput.focus();
    startTime = Date.now();
    timerInterval = setInterval(updateTimer, 1000);
}

function updateTimer() {
    const elapsed = Math.floor((Date.now() - startTime) / 1000);
    timerDisplay.textContent = `Time: ${timeLimit - elapsed}s`;

    if (elapsed >= timeLimit) finishTest();
}

function handleInput(e) {
    currentInput = e.target.value;

    if (currentInput === words[currentWordIndex]) {
        currentWordIndex++;
        currentInput = "";
        textInput.value = "";
    }

    if (currentWordIndex === words.length) finishTest();
    renderText();
}

function finishTest() {
    clearInterval(timerInterval);
    const elapsedTime = (Date.now() - startTime) / 1000;
    const wpm = Math.round((currentWordIndex / elapsedTime) * 60);

    textInput.style.display = "none";
    endScreen.style.display = "block";
    endWpm.textContent = `Words Per Minute: ${wpm}`;
}

function resetTest() {
    currentWordIndex = 0;
    currentInput = "";
    clearInterval(timerInterval);

    textInput.value = "";
    textInput.style.display = "none";
    startBtn.style.display = "block";
    endScreen.style.display = "none";
    document.getElementById("stats").style.display = "none";
    timerDisplay.textContent = "Time: 0s";
    wpmDisplay.textContent = "WPM: 0";
}

textInput.addEventListener("input", handleInput);
