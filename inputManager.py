class InputManager:
    def __init__(self):
        pass
    
    def getMoveIp(self):
        
        start = input("Enter piece to move (e.g. E2)")
        end = input("Enter Move location (e.g. E4)")
        
        return start.strip(), end.strip()
    
    def ipToBoardCoords(self, startStr, endStr):
        if len(startStr) == 2 or len(endStr) == 2:
            startColumn = ord(startStr[0].upper()) - ord('A') #convert character to number for coords
            startRow = 8 - int(startStr[1])
            
            endColumn = ord(endStr[0].upper()) - ord('A')
            EndRow = 8 - int(endStr[1])
            
            return (startRow, startColumn), (EndRow, endColumn)
        else:
            return None, None