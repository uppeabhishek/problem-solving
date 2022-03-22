class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        li = ['a'] * n
        k = k - n
        for i in range(n - 1, -1, -1):
            if k > 25:
                li[i] = 'z'
                k -= 25
            else:
                li[i] = chr(97 + k)
                break
        
        return "".join(li)
        