class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        first, prev = nums[0], nums[0]
        
        result = []
        
        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                if first == prev:
                    result.append(str(first))
                else:
                    result.append(str(first) + "->" + str(prev))
                first, prev = nums[i], nums[i]
            else:
                prev = nums[i]
                
        if first == prev:
            result.append(str(first))
        else:
            result.append(str(first) + "->" + str(prev))
        
        return result