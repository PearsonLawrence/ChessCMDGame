import unittest 
from Board import Board
from piece import Piece

class Test_Board(unittest.TestCase):
    def setUp(self):
        return super().setUp()
        
    def test_SetupBoard(self):
        board = Board() #Calls setupboard
        for column in range(8): #Tests pawn setup
            self.assertTrue(board.grid[1][column] is not None)
            self.assertEqual(board.grid[1][column].name, 'P')
            self.assertEqual(board.grid[1][column].color, 'b')
            
            self.assertTrue(board.grid[6][column] is not None)
            self.assertEqual(board.grid[6][column].name, 'P')
            self.assertEqual(board.grid[6][column].color, 'w')
            
        #Tests rook setup
        self.assertEqual(board.grid[0][0].name, 'R')
        self.assertEqual(board.grid[0][0].color, 'b')
        self.assertEqual(board.grid[0][7].name, 'R')
        self.assertEqual(board.grid[0][7].color, 'b')
        self.assertEqual(board.grid[7][0].name, 'R')
        self.assertEqual(board.grid[7][0].color, 'w')
        self.assertEqual(board.grid[7][7].name, 'R')
        self.assertEqual(board.grid[7][7].color, 'w')
        
        self.assertEqual(board.grid[0][1].name, 'N')
        self.assertEqual(board.grid[0][1].color, 'b')
        self.assertEqual(board.grid[0][6].name, 'N')
        self.assertEqual(board.grid[0][6].color, 'b')
        self.assertEqual(board.grid[7][1].name, 'N')
        self.assertEqual(board.grid[7][1].color, 'w')
        self.assertEqual(board.grid[7][6].name, 'N')
        self.assertEqual(board.grid[7][6].color, 'w')
        
        self.assertEqual(board.grid[0][2].name, 'B')
        self.assertEqual(board.grid[0][2].color, 'b')
        self.assertEqual(board.grid[0][5].name, 'B')
        self.assertEqual(board.grid[0][5].color, 'b')
        self.assertEqual(board.grid[7][2].name, 'B')
        self.assertEqual(board.grid[7][2].color, 'w')
        self.assertEqual(board.grid[7][5].name, 'B')
        self.assertEqual(board.grid[7][5].color, 'w')
        
        self.assertEqual(board.grid[0][3].name, 'Q')
        self.assertEqual(board.grid[0][3].color, 'b')
        self.assertEqual(board.grid[7][3].name, 'Q')
        self.assertEqual(board.grid[7][3].color, 'w')
        
        self.assertEqual(board.grid[0][4].name, 'K')
        self.assertEqual(board.grid[0][4].color, 'b')
        self.assertEqual(board.grid[7][4].name, 'K')
        self.assertEqual(board.grid[7][4].color, 'w')
    
    def test_isKingAlive(self):
        board = Board()
        self.assertTrue(board.isKingAlive('w'))
        self.assertTrue(board.isKingAlive('b'))
        
        board.grid[7][4] = None 
        self.assertTrue(board.grid[7][4] == None )   
        self.assertFalse(board.isKingAlive('w'))   
        
        board.grid[0][4] = None 
        self.assertTrue(board.grid[0][4] == None )   
        self.assertFalse(board.isKingAlive('b'))   
        
        
    def test_checkValidMove(self):
        board = Board()
        
        self.assertTrue(board.checkValidMove((6,0), (5,0))) #a2 to a3
        self.assertTrue(board.checkValidMove((6,0), (4,0))) #a2 to a4
        
        #Edge case
        self.assertFalse(board.checkValidMove((6,0), (6,0))) #check to see if piece can move on itself
        self.assertFalse(board.checkValidMove((7,1), (6,3))) #b1 to d2
        self.assertFalse(board.checkValidMove((7,0), (8,0))) #try moving rook out of bounds
        self.assertFalse(board.checkValidMove((0,3), (3,6))) #d8 to g5 Path blocked
        
        #Remove black row of pawns for testing
        board.grid[1][0] = None 
        board.grid[1][1] = None 
        board.grid[1][2] = None 
        board.grid[1][3] = None 
        board.grid[1][4] = None 
        board.grid[1][5] = None 
        board.grid[1][6] = None 
        board.grid[1][7] = None 
        
        self.assertTrue(board.checkValidMove((0,3), (3,6))) #d8 to g5
        self.assertTrue(board.checkValidMove((0,0), (3,0))) #a8 to a5
        self.assertTrue(board.checkValidMove((0,2), (3,5))) #c8 to f5
        self.assertTrue(board.checkValidMove((0,4), (1,3))) #e8 to d7
        self.assertTrue(board.checkValidMove((0,6), (2,5))) #g8 to f6
        
        #Edge case
        self.assertFalse(board.checkValidMove((0,2), (1,2))) #c8 to c7
        self.assertFalse(board.checkValidMove((0,0), (1,1))) #a8 to b7
        
        #self.assertTrue(board.checkValidMove((0,3), (0,4))) #d8 to e8 (To be used for presentation purposes)
        #self.assertFalse(board.checkValidMove((0,3), (0,4))) #d8 to e8 (To be used for presentation purposes)
    
if __name__ == '__main__':
    unittest.main()