from copy import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        tempResult = []
        result = []
        
        def recursion(target, index):
                        
            if target == 0:
                result.append(copy(tempResult))
                return
            
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                if target >= candidate:
                    tempResult.append(candidate)
                    recursion(target - candidate, i)
                    tempResult.pop()
            
        
        recursion(target, 0)
        return result
                