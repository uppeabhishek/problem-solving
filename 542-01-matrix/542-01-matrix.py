class Solution:
    
    def isValid(self, i, j, rows, cols):
        return not (i < 0 or j < 0 or i == rows or j == cols)
    
    def updateMatrixHelper(self, mat, zeros, rows, cols):
            
        queue = deque([])
        
        for zero in zeros:
            queue.append(zero)
        
        paths = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        
        visited = set([queue[0][0], queue[0][1]])

        while len(queue):
            i, j = queue.popleft()    
            
            for path in paths:
                i1, j1 = path[0] + i, path[1] + j
                current = (i1, j1)
                
                if self.isValid(i1, j1, rows, cols) and current not in visited:
                    if mat[i1][j1] != 0:
                        if mat[i][j] == 0:
                            mat[i1][j1] = 1
                        else:
                            mat[i1][j1] = mat[i][j] + 1            
                    queue.append(current)
                visited.add(current)
                    
                
            
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        zeros = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    zeros.append((i, j))
                
        self.updateMatrixHelper(mat, zeros, len(mat), len(mat[0]))
        
        return mat
    
        