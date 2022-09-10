class Solution:
    
    def __init__(self):
        self.size = 3
        
    def addRowColDiagonal(self, row, col, playerdict_row, playerdic_col, diagonal_player):
        size = self.size
        
        playerdict_row[row] += 1
        playerdic_col[col] += 1
                
        if row == col:
            diagonal_player[1] += 1
        
        if row + col == size - 1:
            diagonal_player[2] += 1
        
        if playerdict_row[row] == size or playerdic_col[col] == size or diagonal_player[1] == size or diagonal_player[2] == size:
            return True
        
        return False
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        playera_row, playera_col, playerb_row, playerb_col = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        
        diagonal_playera, diagonal_playerb = defaultdict(int), defaultdict(int)
        
        playera = True
        
        count = 0
        
        for row, col in moves:
            if playera:
                if self.addRowColDiagonal(row, col, playera_row, playera_col, diagonal_playera):
                    return 'A'
            else:
                if self.addRowColDiagonal(row, col, playerb_row, playerb_col, diagonal_playerb):
                    return 'B'
            
            count += 1
            playera = not playera
    
        if count == self.size * self.size:
            return "Draw"
    
        return "Pending"
                
                