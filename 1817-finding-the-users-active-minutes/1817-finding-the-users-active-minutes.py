class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        dic = defaultdict(set)
        
        for i, j in logs:
            dic[i].add(j)
        
        result = [0] * k
        
        for val in dic.values():
            result[len(val) - 1] += 1
            
        return result