class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i, j, res = 0, len(columnTitle) - 1, 0
        while j >= 0:
            res+=math.pow(26, j) * (ord(columnTitle[i]) - 64)
            i+=1
            j-=1
        return int(res)