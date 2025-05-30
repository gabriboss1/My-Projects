import React from "react";
import { Chessboard } from "react-chessboard";

const ChessboardComponent = ({ position, onPieceDrop, boardWidth = 400 }) => (
  <Chessboard
    position={position}
    onPieceDrop={onPieceDrop}
    boardWidth={boardWidth}
    boardOrientation="white"
    id="main-chessboard"
  />
);

export default ChessboardComponent;
