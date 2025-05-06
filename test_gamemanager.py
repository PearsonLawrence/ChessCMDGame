import unittest 
from gameManager import GameManager

class Test_InputManager(unittest.TestCase):
    
    def setUp(self):
        return super().setUp()
    
    def test_changeTurn(self):
        gm = GameManager()
        self.assertEqual(gm.turn, 'w')
        gm.changeTurn()
        self.assertEqual(gm.turn, 'b')
        gm.changeTurn()
        self.assertEqual(gm.turn, 'w')
        
    
if __name__ == '__main__':
    unittest.main()