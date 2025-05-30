import React from "react";

const GameStatus = ({ game, statusText }) => {
  if (!game) return null;

  let message = statusText || "";

  if (game.isGameOver()) {
    if (game.in_checkmate()) {
      message = `Checkmate! ${game.turn() === "w" ? "Black" : "White"} wins.`;
    } else if (game.in_stalemate()) {
      message = "Draw by stalemate.";
    } else if (game.in_threefold_repetition()) {
      message = "Draw by threefold repetition.";
    } else if (game.insufficient_material()) {
      message = "Draw due to insufficient material.";
    } else if (game.in_draw()) {
      message = "Draw.";
    } else {
      message = "Game over.";
    }
  } else if (game.in_check()) {
    message = `${game.turn() === "w" ? "White" : "Black"} is in check.`;
  } else if (!message) {
    message = `${game.turn() === "w" ? "White" : "Black"} to move.`;
  }

  return <div className="game-status">{message}</div>;
};

export default GameStatus;
