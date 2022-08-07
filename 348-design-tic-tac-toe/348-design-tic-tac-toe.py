class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        
    def move(self, row: int, col: int, player: int) -> int:
        
        self.board[row][col] = player
        
        r1, c1, dia1, dia2 = True, True, True, True
                   
        
        for i in range(len(self.board)):
            if self.board[row][i] != player:
                r1 = False
        
            if self.board[i][col] != player:
                c1 = False
            
            if self.board[i][i] != player:
                dia1 = False
            
            if self.board[i][len(self.board)-i-1] != player:
                dia2 = False
        
        return player if r1 or c1 or dia1 or dia2 else 0
            
            

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)