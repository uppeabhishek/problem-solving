class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, res = 0, 0, 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i+=1
                j+=1
                res+=1
            else:
                j+=1
        
        return res