class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        array = []
        for i in range(len(mat)):
            cnt = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    cnt += 1
            array.append((cnt, i))
    
        array.sort(key = lambda k: k[0])
        
        return [ele[1] for ele in array][:k]
