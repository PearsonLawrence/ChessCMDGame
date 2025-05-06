from Board import Board
from inputManager import InputManager
from piece import Piece

class GameManager:
    def __init__(self):
        self.board = Board()
        self.ip = InputManager()
        self.turn = 'w' #white for starting
        
    def changeTurn(self):
        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'
        
    
    def runGame(self):
        while True:
            self.board.render()
            outstr = ""
            if not self.board.isKingAlive('w'):
                outstr = "Black wins! White king has been captured!"
                print(outstr)
                return outstr
            if not self.board.isKingAlive('b'):
                outstr = "White wins! Black king has been captured!"
                print(outstr)
                return outstr
            
            if self.turn == 'w':
                print("Whites turn")
            else:
                print("Blacks turn")
                
            startStr, endStr = self.ip.getMoveIp()
            startPos, endPos = self.ip.ipToBoardCoords(startStr, endStr)
            
            
            if startPos is None or endPos is None :
                print("Invalid Selection")
                continue
                
            piece = self.board.grid[startPos[0]][startPos[1]]
            if (piece is None) or (piece.color != self.turn):
                print("Invalid Selection")
                continue
            
            if self.board.checkValidMove(startPos, endPos):
                
                if self.board.grid[endPos[0]][endPos[1]] is not None:
                    if self.turn == 'w':
                        print("White Takes a Piece")
                    else:
                        print("Black Takes a Piece")
                        
                self.board.grid[endPos[0]][endPos[1]] = piece
                self.board.grid[startPos[0]][startPos[1]] = None
                self.changeTurn()
            
            
            