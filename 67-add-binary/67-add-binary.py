class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a), len(b)
        
        b = b.zfill(i)
        a = a.zfill(j)
        
        rem = 0
    
        i = len(a) - 1
        j = len(b) - 1
        
        result = deque([])
        
        while i > -1 and j > -1:
            
            a1, b1 = a[i], b[j]
            
            if a1 == '1' and b1 == '1':
                if rem == 0:
                    result.appendleft(0)
                    rem = 1
                else:
                    result.appendleft(1)
            elif a1 == '1' or b1 == '1':
                if rem == 0:
                    result.appendleft(1)
                else:
                    result.appendleft(0)
                    rem = 1
            else:
                result.appendleft(rem)
                rem = 0
            
            i -= 1
            j -= 1
        
        if rem:
            result.appendleft(rem)
        
        return "".join(list(map(str, result)))
            