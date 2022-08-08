from functools import cmp_to_key

def compare(a, b):
    first = str(a) + str(b)
    second = str(b) + str(a)
    
    if first > second:
        return -1
    elif first < second:
        return 1
    
    return 0
    
class Solution:
    
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return '0'
        nums.sort(key = cmp_to_key(compare))
        return "".join(list(map(str, nums)))