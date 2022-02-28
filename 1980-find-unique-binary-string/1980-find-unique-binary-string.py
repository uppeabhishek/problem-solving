class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        le = len(nums[0])
        se = set()
        for num in nums:
            se.add(int(num, 2))
        
        for i in range(0, 2 ** le, 1):
            if i not in se:
                return str(bin(i)[2:].zfill(le))