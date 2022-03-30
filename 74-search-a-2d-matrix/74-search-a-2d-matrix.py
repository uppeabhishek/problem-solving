class Solution:
    def bsearch(self, m, target):
        low, high = 0, len(m) - 1
        while low <= high:
            mid = (low + high) // 2
            if m[mid] == target:
                return True
            elif target < m[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.bsearch(matrix[i], target):
                return True
        
        return False
        