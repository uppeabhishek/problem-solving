class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        
        i, j = 0, n - k - 1
        
        while i <= j:
            swap(i, j)
            i += 1
            j -= 1
        
        i, j = n - k, n - 1
        
        while i <= j:
            swap(i, j)
            i += 1
            j -= 1
            
        
        i, j = 0, n - 1
        
        while i <= j:
            swap(i, j)
            i += 1
            j -= 1
        
        