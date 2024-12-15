# 2/30/2024
# This was a fun project I did to use my spare time. The main goal was to try to make some basic Artificial Intelligence, which was implemented in the gamemode playing against the Computer.
# I still haven't won in that gamemode.


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic-Tac-Toe</title>
    <style>
        body {
            margin: 0;
            font-family: 'Arial', sans-serif;
            background-color: #f0f4f8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
        }

        .game-container {
            text-align: center;
            background: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            display: none;
            width: 400px;
        }

        h1 {
            font-size: 2.5rem;
            color: #3498db;
            margin-bottom: 20px;
        }

        .board {
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-template-rows: repeat(3, 100px);
            gap: 15px;
            justify-content: center;
            margin: 0 auto;
        }

        .cell {
            width: 100px;
            height: 100px;
            background-color: #ecf0f1;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 2rem;
            font-weight: bold;
            color: #2c3e50;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .cell:hover {
            background-color: #bdc3c7;
        }

        .cell.clicked {
            pointer-events: none;
        }

        .reset-btn, .start-btn {
            margin-top: 20px;
            padding: 12px 25px;
            background-color: #3498db;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .reset-btn:hover, .start-btn:hover {
            background-color: #2980b9;
        }

        .result-message {
            margin-top: 20px;
            font-size: 1.8rem;
            color: #2ecc71;
        }

        .result-message span {
            font-size: 2.5rem;
            font-weight: bold;
        }

        .title-screen {
            text-align: center;
            background-color: #ffffff;
            color: #333;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        }

        .title-screen h1 {
            font-size: 3rem;
            color: #3498db;
        }

        .title-screen p {
            font-size: 1.5rem;
            color: #7f8c8d;
        }

        .options {
            margin-top: 20px;
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        .options button {
            padding: 12px 25px;
            background-color: #3498db;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .options button:hover {
            background-color: #2980b9;
        }

    </style>
</head>
<body>
    <div class="title-screen" id="titleScreen">
        <h1>Tic-Tac-Toe</h1>
        <p>Choose your game mode:</p>
        <div class="options">
            <button onclick="startGame('human')">Play with Friend</button>
            <button onclick="startGame('computer')">Play against Computer</button>
        </div>
    </div>

    <div class="game-container" id="gameContainer">
        <h1>Tic-Tac-Toe</h1>
        <div class="board" id="board">
            <div class="cell" data-index="0"></div>
            <div class="cell" data-index="1"></div>
            <div class="cell" data-index="2"></div>
            <div class="cell" data-index="3"></div>
            <div class="cell" data-index="4"></div>
            <div class="cell" data-index="5"></div>
            <div class="cell" data-index="6"></div>
            <div class="cell" data-index="7"></div>
            <div class="cell" data-index="8"></div>
        </div>
        <button class="reset-btn" id="resetBtn">Reset Game</button>
        <div class="result-message" id="resultMessage"></div>
    </div>

    <script>
        let currentPlayer = "X";
        let gameBoard = Array(9).fill(null);
        let gameOver = false;
        let gameMode = "human";

        const board = document.getElementById("board");
        const resetBtn = document.getElementById("resetBtn");
        const resultMessage = document.getElementById("resultMessage");
        const gameContainer = document.getElementById("gameContainer");
        const titleScreen = document.getElementById("titleScreen");

        function checkWinner() {
            const winPatterns = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6],
            ];

            for (let pattern of winPatterns) {
                const [a, b, c] = pattern;
                if (gameBoard[a] && gameBoard[a] === gameBoard[b] && gameBoard[a] === gameBoard[c]) {
                    return gameBoard[a];
                }
            }
            return gameBoard.includes(null) ? null : "draw";
        }

        function handleCellClick(event) {
            const cell = event.target;
            const index = cell.dataset.index;

            if (gameBoard[index] || gameOver) return;

            gameBoard[index] = currentPlayer;
            cell.textContent = currentPlayer;
            cell.classList.add("clicked");

            const winner = checkWinner();
            if (winner) {
                gameOver = true;
                if (winner === "draw") {
                    resultMessage.innerHTML = "It's a <span>Draw!</span>";
                } else {
                    resultMessage.innerHTML = `${winner} <span>Wins!</span>`;
                }
            } else {
                currentPlayer = currentPlayer === "X" ? "O" : "X";
                if (gameMode === "computer" && currentPlayer === "O") {
                    setTimeout(computerMove, 500);
                }
            }
        }

        function minimax(board, depth, isMaximizing) {
            const winner = checkWinner();
            if (winner === "X") return -10 + depth;
            if (winner === "O") return 10 - depth;
            if (winner === "draw") return 0;

            if (isMaximizing) {
                let maxEval = -Infinity;
                for (let i = 0; i < board.length; i++) {
                    if (!board[i]) {
                        board[i] = "O";
                        const eval = minimax(board, depth + 1, false);
                        board[i] = null;
                        maxEval = Math.max(maxEval, eval);
                    }
                }
                return maxEval;
            } else {
                let minEval = Infinity;
                for (let i = 0; i < board.length; i++) {
                    if (!board[i]) {
                        board[i] = "X";
                        const eval = minimax(board, depth + 1, true);
                        board[i] = null;
                        minEval = Math.min(minEval, eval);
                    }
                }
                return minEval;
            }
        }

        function computerMove() {
            let bestMove = -1;
            let bestValue = -Infinity;

            for (let i = 0; i < gameBoard.length; i++) {
                if (!gameBoard[i]) {
                    gameBoard[i] = "O";
                    const moveValue = minimax(gameBoard, 0, false);
                    gameBoard[i] = null;

                    if (moveValue > bestValue) {
                        bestValue = moveValue;
                        bestMove = i;
                    }
                }
            }

            gameBoard[bestMove] = "O";
            document.querySelector(`.cell[data-index="${bestMove}"]`).textContent = "O";
            document.querySelector(`.cell[data-index="${bestMove}"]`).classList.add("clicked");

            const winner = checkWinner();
            if (winner) {
                gameOver = true;
                if (winner === "draw") {
                    resultMessage.innerHTML = "It's a <span>Draw!</span>";
                } else {
                    resultMessage.innerHTML = `${winner} <span>Wins!</span>`;
                }
            } else {
                currentPlayer = "X";
            }
        }

        function startGame(mode) {
            gameMode = mode;
            gameContainer.style.display = "block";
            titleScreen.style.display = "none";
        }

        function resetGame() {
            gameBoard = Array(9).fill(null);
            gameOver = false;
            currentPlayer = "X";
            resultMessage.innerHTML = "";
            Array.from(document.querySelectorAll(".cell")).forEach(cell => {
                cell.textContent = "";
                cell.classList.remove("clicked");
            });
        }

        Array.from(document.querySelectorAll(".cell")).forEach(cell => {
            cell.addEventListener("click", handleCellClick);
        });

        resetBtn.addEventListener("click", resetGame);
    </script>
</body>
</html>
