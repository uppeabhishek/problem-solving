class Solution {
    
    public boolean valid(int i, int j, int m, int n) {
        return !(i < 0 || j < 0 || i == m || j == n);
    }
    
    public int helper(int i, int j, int[][] grid, int m, int n) {
        int result = 0;
        
        if (!valid(i, j, m, n) || grid[i][j] == 0) {
            return 0;
        }
        
        int val = grid[i][j];
        
        grid[i][j] = 0;
        
        result = Math.max(result, val + helper(i - 1, j, grid, m, n));
        result = Math.max(result, val + helper(i, j - 1, grid, m, n));
        result = Math.max(result, val + helper(i + 1, j, grid, m, n));
        result = Math.max(result, val + helper(i, j + 1, grid, m, n));
        
        grid[i][j] = val;
        
        return result;
    }
    
    public int getMaximumGold(int[][] grid) {
        
        int m = grid.length, n = grid[0].length;
        
        int max_result = 0;
            
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                max_result = Math.max(max_result, helper(i, j, grid, m, n));
            }
        } 
        
        return max_result;
    }
}