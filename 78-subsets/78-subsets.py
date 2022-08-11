class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        i = 0
        
        result = []
        
        for i in range(2 ** len(nums)):
            current = bin(i)[2:].zfill(len(nums))
            
            temp = []
            
            for i, c in enumerate(current):
                if c == '1':
                    temp.append(nums[i]) 
            
            result.append(temp)
            
        return result
        
        