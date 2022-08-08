class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = set([])
                
        for i in range(len(nums) - 2):
            start = nums[i]
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                current_sum = start + nums[j] + nums[k]
                
                if current_sum == 0:
                    result.add((start, nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif current_sum > 0:
                    k -= 1
                else:
                    j += 1
        
        final = []
        
        for ele in result:
            final.append(ele)
        
        return final
            
            
                