class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i])
        
        result = deque([])
        
        current = 1
        
        for i in range(len(nums) - 1, -1, -1):
            
            if i == len(nums) - 1:
                temp = prefix[i - 1]
            elif i == 0:
                temp = current
            else:
                temp = prefix[i - 1] * current
                        
            result.appendleft(temp)
            current = current * nums[i]
            
        return list(result)