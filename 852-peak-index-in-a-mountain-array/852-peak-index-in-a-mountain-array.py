class Solution:
    
    def helper(self, arr, low, high):
        mid = (low + high) // 2
        
        if low > high:
            return 0
                
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        return self.helper(arr, low, mid - 1) or self.helper(arr, mid + 1, high)

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.helper(arr, 1, len(arr) - 2)
        
        
                
                