class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        n = len(nums)        
                
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        
        def nextGreaterElement(ele, i):
            
            minElement, minIndex = sys.maxsize, -1

            for j in range(i, n):
                if nums[j] > ele and nums[j] < minElement:
                    minElement = nums[j]
                    minIndex = j
            
            return minIndex
        
        def helper():
            
            nonlocal nums
            
            i = n - 1
        
            while i > 0:
                if nums[i] > nums[i - 1]:
                    break
                i -= 1

            if i == 0:
                nums.sort()
                return
            
            index = nextGreaterElement(nums[i - 1], i)
            
            swap(i - 1, index)
            
            
            temp = nums[0:i] + sorted(nums[i:])
            
            for i in range(n):
                nums[i] = temp[i]
                
            
        helper()
                
            
        