class Solution:
    
    def isValid(self, i, j, rows, cols):
        return not (i < 0 or j < 0 or i == rows or j == cols)
        
    def floodFillHelper(self, image, i, j, rows, cols, original_color, color, visited):
        paths = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        for path in paths:
            i1, j1 = path[0] + i, path[1] + j
            current = (i1, j1)
            
            if self.isValid(i1, j1, rows, cols) and image[i1][j1] == original_color and current not in visited:
                visited.add((i1, j1))
                image[i1][j1] = color
                self.floodFillHelper(image, i1, j1, rows, cols, original_color, color, visited)
            else:
                visited.add((i1, j1))
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        visited = set([(sr, sc)])
        image[sr][sc] = color
        
        self.floodFillHelper(image, sr, sc, len(image), len(image[0]), original_color, color, visited)
        
        return image
        
        
        
        
        