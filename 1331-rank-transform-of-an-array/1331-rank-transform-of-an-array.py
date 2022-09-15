class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        
        result = [0] * n
        
        arr = sorted([(ele, i) for i, ele in enumerate(arr)])
        
        prev = -sys.maxsize
            
        rank = 0
        
        for ele, index in arr:
            if ele != prev:
                rank += 1
            result[index] = rank
            prev = ele
        
        return result
        
        