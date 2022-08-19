class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        dic = defaultdict(int)
            
        dic[0] = -1
        
        cnt = 0
        
        result = 0
    
        for i, num in enumerate(nums):
            
            if num == 0:
                cnt -= 1
            else:
                cnt += 1
            
            if cnt in dic:
                result = max(result, i - dic[cnt])
            else:
                dic[cnt] = i
            
        
        
        return result
            