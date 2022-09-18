class Solution:
    
    def reverseInt(self, num):
        res = 0
        while num:
            rem = num % 10
            res = res * 10 + rem
            num = num // 10
        return res
    
    def addTwoStrings(self, num1, num2):
        res = deque([])
        rem = 0
        
        i, j = len(num1) - 1, len(num2) - 1
        
        while i >= 0 and j >= 0:
            add = num1[i] + num2[j] + rem
            if add > 9:
                rem = add // 10
                res.appendleft(add % 10)
            else:
                res.appendleft(add)
                rem = 0
            
            i -= 1
            j -= 1
            
        while i >= 0:
            add = num1[i] + rem
            if add > 9:
                rem = add // 10
                res.appendleft(add % 10)
            else:
                res.appendleft(add)
                rem = 0
            
            i -= 1
        
        while j >= 0:
            add = num2[j] + rem
            if add > 9:
                rem = add // 10
                res.appendleft(add % 10)
            else:
                res.appendleft(add)
                rem = 0
            j -= 1
        
        if rem:
            res.appendleft(rem)
        
        return res
        
    def multiply(self, num1: str, num2: str) -> str:
                
        if num1 == '0' or num2 == '0':
            return '0'
        
        m, n = len(num1), len(num2)
        
        result = []
        counter = 0
        
        for i in range(n - 1, -1, -1):
            
            current = deque([])
            
            for _ in range(counter):
                current.append(0)
            
            rem = 0
            
            for j in range(m - 1, -1, -1):
                
                mul = int(num1[j]) * int(num2[i]) + rem
                                             
                if mul > 9:
                    rem = mul // 10
                    mul = mul % 10
                else:
                    rem = 0
                current.appendleft(mul)            
            if rem:
                current.appendleft(rem)
            
            
            result = self.addTwoStrings(result, current)
            counter += 1
            
                    
        return "".join(list(map(str, result)))
        