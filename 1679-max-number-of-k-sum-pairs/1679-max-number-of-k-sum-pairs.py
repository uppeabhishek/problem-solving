class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        cnt = 0
        
        for i, num in enumerate(nums):
            dic[num].append(i)
            
        for num in nums:
            second_num = k - num
            if second_num in dic:
                if num == second_num:
                    if len(dic[num]) > 1:
                        dic[num].pop()
                        dic[num].pop()
                        cnt += 1
                else:
                    if len(dic[num]) > 0 and len(dic[second_num]) > 0:
                        dic[num].pop()
                        dic[second_num].pop()
                        cnt += 1            
        return cnt
                    