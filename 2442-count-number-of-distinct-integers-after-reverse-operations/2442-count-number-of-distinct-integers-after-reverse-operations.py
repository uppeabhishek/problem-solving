class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        def reverse(num):
            current = 0
            
            while num:
                rem = num % 10
                current = current * 10 + rem
                num = num // 10
            
            return current
            
        s = set(nums)
        new_s = set(nums)
        
        for c in s:
            new_s.add(reverse(c))
        
        return len(new_s)
            