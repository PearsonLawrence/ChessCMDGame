import unittest 
from piece import Piece

class Test_Piece(unittest.TestCase):
    
    def setUp(self):
        return super().setUp()
        
    def test_pieceCharacter(self):
      
        piece = Piece('P', 'b')
        self.assertEqual(piece.pieceCharacter(),'P') 
        piece = Piece('R', 'b')
        self.assertEqual(piece.pieceCharacter(),'R') 
        piece = Piece('N', 'b')
        self.assertEqual(piece.pieceCharacter(),'N') 
        piece = Piece('B', 'b')
        self.assertEqual(piece.pieceCharacter(),'B') 
        piece = Piece('Q', 'b')
        self.assertEqual(piece.pieceCharacter(),'Q') 
        piece = Piece('K', 'b')
        self.assertEqual(piece.pieceCharacter(),'K') 
        
        
        piece = Piece('P', 'w')
        self.assertEqual(piece.pieceCharacter(),'P') 
        piece = Piece('R', 'w')
        self.assertEqual(piece.pieceCharacter(),'R') 
        piece = Piece('N', 'w')
        self.assertEqual(piece.pieceCharacter(),'N') 
        piece = Piece('B', 'w')
        self.assertEqual(piece.pieceCharacter(),'B') 
        piece = Piece('Q', 'w')
        self.assertEqual(piece.pieceCharacter(),'Q') 
        piece = Piece('K', 'w')
        self.assertEqual(piece.pieceCharacter(),'K') 
        
        '''This would only be allowed on linux due to special symbol
        piece = Piece('P', 'b')
        self.assertEqual(piece.pieceCharacter(),'♟') 
        piece = Piece('R', 'b')
        self.assertEqual(piece.pieceCharacter(),'♜') 
        piece = Piece('N', 'b')
        self.assertEqual(piece.pieceCharacter(),'♞') 
        piece = Piece('B', 'b')
        self.assertEqual(piece.pieceCharacter(),'♝') 
        piece = Piece('Q', 'b')
        self.assertEqual(piece.pieceCharacter(),'♛') 
        piece = Piece('K', 'b')
        self.assertEqual(piece.pieceCharacter(),'♚') 
        
        
        piece = Piece('P', 'w')
        self.assertEqual(piece.pieceCharacter(),'♙') 
        piece = Piece('R', 'w')
        self.assertEqual(piece.pieceCharacter(),'♖') 
        piece = Piece('N', 'w')
        self.assertEqual(piece.pieceCharacter(),'♘') 
        piece = Piece('B', 'w')
        self.assertEqual(piece.pieceCharacter(),'♗') 
        piece = Piece('Q', 'w')
        self.assertEqual(piece.pieceCharacter(),'♕') 
        piece = Piece('K', 'w')
        self.assertEqual(piece.pieceCharacter(),'♔') 
    '''
    
    def test_checkLegalMove(self):
        piece = Piece('P', 'w')
        #edge
        self.assertFalse(piece.checkLegalMove((6,0), (3,0))) #a2 to a5
        self.assertFalse(piece.checkLegalMove((6,0), (5,1))) #a2 to b3
        
        self.assertTrue(piece.checkLegalMove((6,0), (5,0))) #a2 to a3
        self.assertTrue(piece.checkLegalMove((6,0), (4,0))) #a2 to a4
        
        piece = Piece('R', 'w')
        #edge
        self.assertFalse(piece.checkLegalMove((7,0), (6,1))) #a1 to b2
        
        self.assertTrue(piece.checkLegalMove((7,0), (5,0))) #a1 to a3
        self.assertTrue(piece.checkLegalMove((7,0), (7,2))) #a1 to b1
        
        piece = Piece('N', 'w')
        #edge
        self.assertFalse(piece.checkLegalMove((7,1), (6,1))) #b1 to b2
        self.assertFalse(piece.checkLegalMove((7,1), (7,2))) #b1 to c1
        
        self.assertTrue(piece.checkLegalMove((7,1), (5,2))) #b1 to c3
        self.assertTrue(piece.checkLegalMove((7,1), (6,3))) #b1 to d2
        
        piece = Piece('B', 'w')
        #edge
        self.assertFalse(piece.checkLegalMove((7,2), (6,2))) #c1 to c2
        self.assertFalse(piece.checkLegalMove((7,2), (7,3))) #c1 to d1
        
        self.assertTrue(piece.checkLegalMove((7,2), (5,4)))  #c1 to e3
        
        piece = Piece('Q', 'w')
        #edge
        self.assertFalse(piece.checkLegalMove((7,3), (5,4))) #d1 to e3
        self.assertFalse(piece.checkLegalMove((7,3), (6,5))) #d1 to f2
        
        self.assertTrue(piece.checkLegalMove((7,3), (3,3)))  #d1 to d3
        self.assertTrue(piece.checkLegalMove((7,3), (7,0)))  #d1 to a1
        self.assertTrue(piece.checkLegalMove((7,3), (4,0)))  #d1 to a4
        
        piece = Piece('K', 'w')
        #edge
        self.assertFalse(piece.checkLegalMove((7,4), (5,4))) #e1 to e3
        
        self.assertTrue(piece.checkLegalMove((7,4), (6,4))) #e1 to e2
        self.assertTrue(piece.checkLegalMove((7,4), (7,3))) #e1 to d1
    
if __name__ == '__main__':
    unittest.main()