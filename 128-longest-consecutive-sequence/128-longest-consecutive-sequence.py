class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            
        if not len(nums):
            return 0
        
        s = set(nums)
        dic = {}
        
        for num in s:
            
            cnt = 1
            i = 1
            
            while num - i in s:
                if num - i in dic:
                    cnt += dic[num - i]
                    break
                
                i += 1
                cnt += 1
            
            dic[num] = cnt
            

        return max(dic.values())
            
                
            
                            
                
        
                