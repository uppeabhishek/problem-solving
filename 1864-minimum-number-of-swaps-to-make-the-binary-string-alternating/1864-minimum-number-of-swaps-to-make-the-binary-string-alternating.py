class Solution:
    def minSwaps(self, s: str) -> int:
        
        n = len(s)
        
        zeros, ones = 0, 0
        
        for c in s:
            if c == "0":
                zeros += 1
            else:
                ones += 1
        
        if abs(zeros - ones) > 1:
            return -1
            
        a, b = '0', '1'
        cnt1, cnt2 = 0, 0
        o1, z1 = 0, 0
        o2, z2 = 0, 0
        
        for i in range(n):
            
            if a != s[i]:
                cnt1 += 1
                if s[i] == '0':
                    z1 += 1
                else:
                    o1 += 1
            
            if b != s[i]:
                cnt2 += 1
                if s[i] == '0':
                    z2 += 1
                else:
                    o2 += 1
                
            a = '1' if a == '0' else '0'
            b = '1' if b == '0' else '0'
             
        if cnt1 < cnt2:
            if o1 == z1:
                diff = cnt1
            else:
                diff = cnt2
        else:
            if o2 == z2:
                diff = cnt2
            else:
                diff = cnt1
                
        if diff & 1 == 1:
            diff += 1
        
        
        return diff // 2
            