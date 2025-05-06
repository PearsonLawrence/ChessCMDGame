
class Piece:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def pieceCharacter(self):
        character = {
            'w': {'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔'}, #White pieces
            'b': {'P': '♟', 'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚'} #black pieces
        }
        return character[self.color][self.name]
    
    def checkLegalMove(self, startpos, endpos):
        startRow, startColumn = startpos
        endRow, endColumn = endpos
        
        xMovement = endRow - startRow
        yMovement = endColumn - startColumn
        
        if self.name == 'P': #pawn (obsolete)
            dir = 0
            if self.color == 'w':
                dir = -1
            else:
                dir = 1
                
            if xMovement == dir and yMovement == 0: # 1 square move
                return True
            
            if self.color == 'w' and startRow == 6 and xMovement == -2 and yMovement == 0:
                return True
            if self.color == 'b' and startRow == 1 and xMovement == 2 and yMovement == 0:
                return True
           
            return False

        if self.name == 'R': #Rook
            if xMovement == 0 or yMovement == 0: #as long as only one axis is moved
                return True
            return False
        
        if self.name == 'N': #knight
            if  (abs(xMovement) == 2 and abs(yMovement) == 1) or (abs(xMovement) == 1 and abs(yMovement) == 2): #+- up 2 over 1 ir +- up 1 over 2
                return True
            return False
        
        if self.name == 'B': #bishop
            if abs(xMovement) == abs(yMovement): #diagonal means equal movement on both axis
                return True
            return False
        
        if self.name == 'K': #king
            if abs(xMovement) <= 1 and abs(yMovement) <= 1: #king move any direction as long as its <= 1
                return True
            return False
        
        if self.name == 'Q': #Queen
            if xMovement == 0 or yMovement == 0 or abs(xMovement) == abs(yMovement): #Queen can move in any direction so its the rook and bishop movement together
                return True
            return False
        return False #for invalid
                