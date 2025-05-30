import React, { useState, useRef } from "react";
import { Chessboard } from "react-chessboard";
import { Chess } from "chess.js";
import "./styles/App.css";

function getRandomMove(game) {
  const moves = game.moves();
  if (moves.length === 0) return null;
  return moves[Math.floor(Math.random() * moves.length)];
}

function App() {
  const [game, setGame] = useState(new Chess());
  const [fen, setFen] = useState("start");
  const boardRef = useRef();

  function safeGameMutate(modify) {
    setGame((g) => {
      const update = new Chess(g.fen());
      modify(update);
      setFen(update.fen());
      return update;
    });
  }

  function onDrop(sourceSquare, targetSquare) {
    const moves = game.moves({ square: sourceSquare, verbose: true });
    const isLegal = moves.some(
      (move) =>
        move.from === sourceSquare &&
        move.to === targetSquare
    );
    if (!isLegal) return false;

    let move = null;
    safeGameMutate((gameInstance) => {
      move = gameInstance.move({
        from: sourceSquare,
        to: targetSquare,
        promotion: "q"
      });
    });

    if (move === null) return false;

    setTimeout(() => {
      safeGameMutate((gameInstance) => {
        if (!gameInstance.isGameOver()) {
          const aiMove = getRandomMove(gameInstance);
          if (aiMove) gameInstance.move(aiMove);
        }
      });
    }, 500);

    return true;
  }

  function isDraggablePiece({ piece, sourceSquare }) {
    if (game.isGameOver()) return false;
    const turn = game.turn();
    if ((turn === "w" && piece.startsWith("w")) || (turn === "b" && piece.startsWith("b"))) {
      const moves = game.moves({ square: sourceSquare, verbose: true });
      return moves.length > 0;
    }
    return false;
  }

  function isSquareDroppable({ sourceSquare, targetSquare }) {
    const moves = game.moves({ square: sourceSquare, verbose: true });
    return moves.some((move) => move.to === targetSquare);
  }

  return (
    <div className="chess-app-bg">
      <div className="chess-card">
        <div className="chess-title">Chess</div>
        <Chessboard
          id="BasicBoard"
          position={fen}
          onPieceDrop={onDrop}
          boardWidth={400}
          ref={boardRef}
          arePiecesDraggable={true}
          isDraggablePiece={isDraggablePiece}
          isSquareDroppable={isSquareDroppable}
          boardOrientation="white"
          animationDuration={200}
          customBoardStyle={{
            borderRadius: 12,
            boxShadow: "0 4px 16px 0 rgba(99,102,241,0.10)",
          }}
          className="chessboard-custom"
        />
        <div className="chess-status">
          {game.isGameOver() && (
            <div>
              Game Over:{" "}
              {game.isCheckmate()
                ? (game.turn() === "w" ? "Black" : "White") + " wins by checkmate."
                : "Draw"}
            </div>
          )}
        </div>
        <button
          className="chess-restart-btn"
          onClick={() => {
            setGame(new Chess());
            setFen("start");
          }}
        >
          Restart Game
        </button>
      </div>
    </div>
  );
}

export default App;
