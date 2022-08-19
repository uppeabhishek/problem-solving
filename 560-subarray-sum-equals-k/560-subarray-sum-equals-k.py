class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        dic[0] = [-1]
        
        current = 0
        
        res = 0
        
        for i, num in enumerate(nums):
            current += num
            
            if current - k in dic:
                res += len(dic[current - k])
                
            dic[current].append(i)

                
        return res
            
            