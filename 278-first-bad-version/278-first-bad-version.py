# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    
    def firstBadVersionHelper(self, low, high):
        
        if low > high:
            return low
            
        mid = (low + high) // 2
        
        if isBadVersion(mid):
            return self.firstBadVersionHelper(low, mid - 1)
        
        return self.firstBadVersionHelper(mid + 1, high)
        
    
    def firstBadVersion(self, n: int) -> int:
        return self.firstBadVersionHelper(1, n)