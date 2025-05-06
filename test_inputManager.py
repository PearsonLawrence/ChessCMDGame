import unittest 
from inputManager import InputManager

class Test_InputManager(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_ipToBoardCoords(self):
        ip = InputManager()
        start, end = ip.ipToBoardCoords("E2", "E4")
        
        self.assertEqual(start, (6,4))
        self.assertEqual(end, (4,4))

        start, end = ip.ipToBoardCoords("b7", "c6")
        self.assertEqual(start, (1,1))
        self.assertEqual(end, (2,2))
        
        #edge
        start, end = ip.ipToBoardCoords("A1", "H8")
        self.assertEqual(start, (7,0))
        self.assertEqual(end, (0,7))
        
        start, end = ip.ipToBoardCoords("ESD", "EDS")
        self.assertIsNone(start)
        self.assertIsNone(end)
    
if __name__ == '__main__':
    unittest.main()