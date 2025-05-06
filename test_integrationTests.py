import unittest 
from inputManager import InputManager
from gameManager import GameManager
from piece import Piece
from Board import Board
class Test_IntegrationTests(unittest.TestCase):
    
    def setUp(self):
        return super().setUp()
    
    def test_inputAndMove(self):
        board = Board()
        im = InputManager()
        gm = GameManager()
    
        startInput, endInput = "A2", "A4" #Wants to move pawn on a2 to a4
        start, end = im.ipToBoardCoords(startInput, endInput)
        piece = board.grid[start[0]][start[1]]
        
        self.assertIsNotNone(piece)
        self.assertEqual(piece.name, 'P')  # Should be pawn
        self.assertEqual(piece.color, 'w')   # Should be white
        
        self.assertIsNone(board.grid[end[0]][end[1]]) #validate that the end point is null (no piece)
        self.assertTrue(board.checkValidMove(start, end)) #ensure move is valid
        
        board.grid[end[0]][end[1]] = piece  #Moves pawn to new position
        board.grid[start[0]][start[1]] = None #Clears the start position and sets piece to none
        self.assertIsNone(board.grid[start[0]][start[1]]) #ensure start is cleaned up
        self.assertEqual(board.grid[end[0]][end[1]].name, 'P') #ensure end position is now a pawn
        gm.changeTurn()
        self.assertEqual(gm.turn, 'b')
        
        
        
    def test_TradePawns(self):
        board = Board()
        im = InputManager()
        gm = GameManager()
    
        startInput, endInput = "A2", "A4" #Wants to move pawn on a2 to a4
        start, end = im.ipToBoardCoords(startInput, endInput)
        piece = board.grid[start[0]][start[1]]
        
        self.assertIsNotNone(piece)
        self.assertEqual(piece.name, 'P')  # Should be pawn
        self.assertEqual(piece.color, 'w')   # Should be white
        
        self.assertIsNone(board.grid[end[0]][end[1]]) #validate that the end point is null (no piece)
        self.assertTrue(board.checkValidMove(start, end)) #ensure move is valid
        
        board.grid[end[0]][end[1]] = piece  #Moves pawn to new position
        board.grid[start[0]][start[1]] = None #Clears the start position and sets piece to none
        self.assertIsNone(board.grid[start[0]][start[1]]) #ensure start is cleaned up
        self.assertEqual(board.grid[end[0]][end[1]].name, 'P') #ensure end position is now a pawn
        
        #Before every change turn it checks win condition
        self.assertTrue(board.isKingAlive('w')) #Checks to see if king is alive
        self.assertTrue(board.isKingAlive('b')) #Checks to see if king is alive 
        
        gm.changeTurn()
        self.assertEqual(gm.turn, 'b')
        
        startInput, endInput = "B7", "B5" #Wants to move pawn on b7 to b5
        start, end = im.ipToBoardCoords(startInput, endInput)
        piece = board.grid[start[0]][start[1]]
        
        self.assertIsNotNone(piece)
        self.assertEqual(piece.name, 'P')  # Should be pawn
        self.assertEqual(piece.color, 'b')   # Should be white
        
        self.assertIsNone(board.grid[end[0]][end[1]]) #validate that the end point is null (no piece)
        self.assertTrue(board.checkValidMove(start, end)) #ensure move is valid
        
        board.grid[end[0]][end[1]] = piece  #Moves pawn to new position
        board.grid[start[0]][start[1]] = None #Clears the start position and sets piece to none
        self.assertIsNone(board.grid[start[0]][start[1]]) #ensure start is cleaned up
        self.assertEqual(board.grid[end[0]][end[1]].name, 'P') #ensure end position is now a pawn
        gm.changeTurn()
        self.assertEqual(gm.turn, 'w')
        
        
        startInput, endInput = "A4", "B5" #wants to move pawn on A4 to B5 taking the black pawn
        start, end = im.ipToBoardCoords(startInput, endInput)
        piece = board.grid[start[0]][start[1]]
        
        self.assertIsNotNone(piece)
        self.assertEqual(piece.name, 'P')  # Should be pawn
        self.assertEqual(piece.color, 'w')   # Should be white
        
        self.assertIsNotNone(board.grid[end[0]][end[1]]) #validate that the end point is not none (pawn threat)
        self.assertTrue(board.checkValidMove(start, end)) #ensure move is valid
        
        board.grid[end[0]][end[1]] = piece  #Moves pawn to new position (Takes Piece by overwriting its position with the pawn effectively deleting it)
        board.grid[start[0]][start[1]] = None #Clears the start position and sets piece to none
        self.assertIsNone(board.grid[start[0]][start[1]]) #ensure start is cleaned up
        self.assertEqual(board.grid[end[0]][end[1]].name, 'P') #ensure end position is now a pawn
        gm.changeTurn()
        self.assertEqual(gm.turn, 'b')
    
    
    def test_takeKing(self): #No checkmate feature so simply check to see if it takes the king for now to test win condition
        board = Board()
        im = InputManager()
        gm = GameManager()
        
        board.grid[1][4] = None  # Remove black pawn at E7
        board.grid[6][4] = None  # Remove white pawn at E2
        
        startInput, endInput = "D1", "E2" # wants to Move queen on d1 to e2
        start, end = im.ipToBoardCoords(startInput, endInput)
        piece = board.grid[start[0]][start[1]]
        
        self.assertIsNotNone(piece)
        self.assertEqual(piece.name, 'Q')  # Should be queen
        self.assertEqual(piece.color, 'w')   # Should be white
        
        self.assertTrue(board.checkValidMove(start, end)) #ensure move is valid
        
        board.grid[end[0]][end[1]] = piece  #Moves queen to new position 
        board.grid[start[0]][start[1]] = None #Clears the start position and sets piece to none
        self.assertIsNone(board.grid[start[0]][start[1]]) #ensure start is cleaned up
        self.assertEqual(board.grid[end[0]][end[1]].name, 'Q') #ensure end position is now a queen
        
        
        self.assertTrue(board.isKingAlive('w')) #Checks to see if king is alive
        self.assertTrue(board.isKingAlive('b')) #Checks to see if king is alive
        
        gm.changeTurn()
        self.assertEqual(gm.turn, 'b')
        
        #Just a fluff move so white can take king
        startInput, endInput = "C7", "C6" #Wants to move pawn on c7 to c6
        start, end = im.ipToBoardCoords(startInput, endInput)
        piece = board.grid[start[0]][start[1]]
        board.grid[end[0]][end[1]] = piece  #Moves pawn to new position 
        board.grid[start[0]][start[1]] = None #Clears the start position and sets piece to none
        
        
        self.assertTrue(board.isKingAlive('w')) #Checks to see if king is alive
        self.assertTrue(board.isKingAlive('b')) #Checks to see if king is alive
        
        gm.changeTurn()
        self.assertEqual(gm.turn, 'w')
        
        startInput, endInput = "E2", "E8" #wants to move queen on e2 to e8 to take king
        start, end = im.ipToBoardCoords(startInput, endInput)
        piece = board.grid[start[0]][start[1]]
        
        self.assertIsNotNone(piece)
        self.assertEqual(piece.name, 'Q')  # Should be queen
        self.assertEqual(piece.color, 'w')   # Should be white
        
        self.assertTrue(board.checkValidMove(start, end)) #ensure move is valid
        
        board.grid[end[0]][end[1]] = piece  #Moves queen to new position taking the king
        board.grid[start[0]][start[1]] = None #Clears the start position and sets piece to none
        self.assertIsNone(board.grid[start[0]][start[1]]) #ensure start is cleaned up
        self.assertEqual(board.grid[end[0]][end[1]].name, 'Q') #ensure end position is now a queen
        
        self.assertTrue(board.isKingAlive('w')) #Checks to see if king is alive
        self.assertFalse(board.isKingAlive('b')) #Fails test and display whites victory
        
        gm.changeTurn()
        self.assertEqual(gm.turn, 'b')
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()