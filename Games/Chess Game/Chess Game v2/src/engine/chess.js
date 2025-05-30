// This is a wrapper for chess.js to allow easy replacement or extension.
import { Chess } from "chess.js";

export function createGame(fen = undefined) {
  return new Chess(fen);
}

export function getMoves(game) {
  return game.moves();
}

export function makeMove(game, move) {
  // move: { from, to, promotion? }
  const result = game.move(move);
  return result;
}

export function isGameOver(game) {
  return game.isGameOver();
}

export function getFen(game) {
  return game.fen();
}
