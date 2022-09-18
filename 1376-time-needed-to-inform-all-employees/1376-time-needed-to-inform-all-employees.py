class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        dictionary = defaultdict(list)
        
        for i, m in enumerate(manager):
            if informTime[i] != 0:
                dictionary[m].append(i)
        
        result = 0
        
        def helper(root, current):
            
            nonlocal result
            
            if root == -1:
                current.append(0)
            else:
                current.append(informTime[root] + current[-1])
            
            for child in dictionary[root]:
                helper(child, current)
        
            result = max(current[-1], result)
            current.pop()
            
        helper(-1, [])
        
        return result