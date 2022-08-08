class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.dict = defaultdict(int)

                    
    def move(self, row: int, col: int, player: int) -> int:
        
        self.board[row][col] = player
        
        d1_key = 'd1_' + str(player)
        d2_key = 'd2_' + str(player)
        key1, key2 = 'r_' + str(row) + '_' + str(player), 'c_' + str(col) + '_' + str(player)
        
        if row == col:
            self.dict[d1_key] += 1
        
        if row + col == len(self.board) - 1:
            self.dict[d2_key] += 1
        
        
        self.dict[key1] += 1
        self.dict[key2] += 1
                
        row_col = self.dict[key1] == len(self.board) or self.dict[key2] == len(self.board)
        diagonal = self.dict[d1_key] == len(self.board) or self.dict[d2_key] == len(self.board)
        
        return player if row_col or diagonal else 0    
            
            

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)