

from piece import Piece
from colorama import init, Fore, Back, Style

init(autoreset=True)

class Board:
    def __init__(self):
        self.grid = []
        
        for _ in range(8):
            row = [None] * 8
            self.grid.append(row)
            
        self.setupBoard()

    def setupBoard(self):
        
        for column in range(8):
            self.grid[1][column] = Piece('P', 'b')
            self.grid[6][column] = Piece('P', 'w')

        self.grid[0][0] = Piece('R', 'b')
        self.grid[0][7] = Piece('R', 'b')
        self.grid[7][0] = Piece('R', 'w')
        self.grid[7][7] = Piece('R', 'w')

        self.grid[0][1] = Piece('N', 'b')
        self.grid[0][6] = Piece('N', 'b')
        self.grid[7][1] = Piece('N', 'w')
        self.grid[7][6] = Piece('N', 'w')
        
        self.grid[0][2] = Piece('B', 'b')
        self.grid[0][5] = Piece('B', 'b')
        self.grid[7][2] = Piece('B', 'w')
        self.grid[7][5] = Piece('B', 'w')

        self.grid[0][3] = Piece('Q', 'b')
        self.grid[7][3] = Piece('Q', 'w')

        self.grid[0][4] = Piece('K', 'b')
        self.grid[7][4] = Piece('K', 'w')

    
    def isKingAlive(self, color):
        for row in self.grid:
            for piece in row:
                if piece is not None and piece.name == 'K' and piece.color == color:
                    return True
        return False
    

    def checkValidMove(self, start, end):
        startRow, startColumn = start
        endRow, endColumn = end
        
        piece = self.grid[startRow][startColumn]
        if piece is None: #Check to see if piece on start location
            print("No piece at start position")
            return False
        if not (0 <= endRow < 8 and 0 <= endColumn < 8): #Check to see if out of bounds
            print("End Position is out of bounds!")
            return False
        
        destinationPiece = self.grid[endRow][endColumn]
        if destinationPiece is not None and destinationPiece.color == piece.color: #check to see if square moving to is occupied
            print("Square occupied by own piece")
            return False
        
        if piece.name != 'P': #Have to abstract pawn logic to handle pawn taking diagonal
            if not piece.checkLegalMove((startRow, startColumn), (endRow, endColumn)): #If not pawn check legal move
                print("Invalid Move")
                return False
            
        if piece.name in ['R', 'B', 'Q']: #Check to see if path is blocked
            xmovement = endRow - startRow
            ymovement = endColumn - startColumn
            if xmovement > 0:
                trackx = 1
            elif xmovement < 0:
                trackx = -1
            else:
                trackx = 0

            if ymovement > 0:
                tracky = 1
            elif ymovement < 0:
                tracky = -1
            else:
                tracky = 0

            currentRow = startRow + trackx
            currentColumn = startColumn + tracky
            cond = True
            while currentRow != endRow or currentColumn != endColumn:
                if not (0 <= currentRow < 8 and 0 <= currentColumn < 8):
                    print("Out of bounds")
                    return False
                if self.grid[currentRow][currentColumn] is not None:
                    print("Path is blocked")
                    return False
                currentRow += trackx
                currentColumn += tracky
                
        elif piece.name == 'P': #If pawn check legal move
            dir = 0
            if piece.color == 'w':
                dir = -1
            else:
                dir = 1
            
            xmovement = endRow - startRow
            ymovement = endColumn - startColumn
            
            if ymovement == 0:
                if destinationPiece is not None:
                    print("pawn cannot move forward into piece")
                    return False
                
                if abs(xmovement) == 2:
                    if (piece.color == 'w' and startRow != 6) or (piece.color == 'b' and startRow != 1):
                        print("Pawn can only move two squares from starting position")
                        return False
                    
                    middle = startRow + dir
                    if self.grid[middle][startColumn] is not None:
                        print("Pawn cant jump over pieces")
                        return False
                    
            elif abs(ymovement) == 1 and xmovement == dir:
                if destinationPiece is None:
                    print("Pawn Cant move diagonal without capturing")
                    return False
                if destinationPiece.color == piece.color:
                    print("Cant capture own piece")
                    return False
            elif not (ymovement == 0 and xmovement == dir or abs(ymovement) == 1 and xmovement == dir):
                print("Invalid Pawn Move")
                return False
        
        return True

    def render(self):
        print("   a  b  c  d  e  f  g  h")
        for row in range(8):
            rowstr = f"{8 - row} "
            for col in range(8):
                piece = self.grid[row][col]

                if (row + col) % 2 == 0:
                    boardColor = Back.LIGHTBLUE_EX
                else:
                    boardColor = Back.BLUE

                if piece:
                    if piece.color == 'b':
                        pieceColor = Fore.LIGHTWHITE_EX
                    else: 
                        pieceColor = Fore.BLACK
                    boardBlock = f"{boardColor}{pieceColor} {piece.pieceCharacter()} {Style.RESET_ALL}"
                else:
                    boardBlock = f"{boardColor}   {Style.RESET_ALL}"  

                rowstr += boardBlock
            print(rowstr + f" {8 - row}")
        print("   a  b  c  d  e  f  g  h")