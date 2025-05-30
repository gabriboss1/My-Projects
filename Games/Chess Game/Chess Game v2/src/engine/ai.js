// Stronger AI: Minimax with material evaluation and depth control

const pieceValues = {
  p: 1,
  n: 3,
  b: 3,
  r: 5,
  q: 9,
  k: 0
};

function evaluateBoard(game) {
  const fen = game.fen();
  const board = fen.split(" ")[0];
  let score = 0;
  for (const char of board) {
    if (char === "/") continue;
    if (char >= "1" && char <= "8") continue;
    const lower = char.toLowerCase();
    const value = pieceValues[lower] || 0;
    score += char === lower ? -value : value;
  }
  return score;
}

// Minimax with alpha-beta pruning
function minimax(game, depth, isMaximizing, alpha, beta) {
  if (depth === 0 || game.isGameOver()) {
    return evaluateBoard(game);
  }

  const moves = game.moves();
  if (isMaximizing) {
    let maxEval = -Infinity;
    for (const move of moves) {
      const gameCopy = new game.constructor(game.fen());
      gameCopy.move(move);
      const evalScore = minimax(gameCopy, depth - 1, false, alpha, beta);
      maxEval = Math.max(maxEval, evalScore);
      alpha = Math.max(alpha, evalScore);
      if (beta <= alpha) break;
    }
    return maxEval;
  } else {
    let minEval = Infinity;
    for (const move of moves) {
      const gameCopy = new game.constructor(game.fen());
      gameCopy.move(move);
      const evalScore = minimax(gameCopy, depth - 1, true, alpha, beta);
      minEval = Math.min(minEval, evalScore);
      beta = Math.min(beta, evalScore);
      if (beta <= alpha) break;
    }
    return minEval;
  }
}

export function getRandomMove(game) {
  const moves = game.moves();
  if (!moves.length) return null;
  const move = moves[Math.floor(Math.random() * moves.length)];
  return move;
}

// Depth can be increased for stronger play (3 is reasonable for browser)
export async function getBestMove(game, depth = 3) {
  const moves = game.moves();
  if (!moves.length) return null;

  let bestMove = null;
  let bestScore = -Infinity;
  for (const move of moves) {
    const gameCopy = new game.constructor(game.fen());
    gameCopy.move(move);
    const score = minimax(gameCopy, depth - 1, false, -Infinity, Infinity);
    if (score > bestScore) {
      bestScore = score;
      bestMove = move;
    }
  }
  return bestMove;
}
