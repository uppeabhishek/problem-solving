from collections import deque
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        
        if num in dic:
            return dic[num]
        
        res = deque([])
        
        index = 0
        
        while num:
            rem = num % 10
            actual_val = (10 ** index) * num 
            
            if rem != 0:
                if actual_val in dic:
                    res.appendleft(dic[actual_val])
                else:
                    if rem <= 3:
                        for _ in range(rem):
                            res.appendleft(dic[(10 ** index)])

                    elif rem == 4:   
                        res.appendleft(dic[(10 ** index) * 5])
                        res.appendleft(dic[(10 ** index)])

                    elif rem == 6:
                        res.appendleft(dic[(10 ** index)])
                        res.appendleft(dic[(10 ** index) * 5])                

                    elif rem == 9:
                        res.appendleft(dic[(10 ** (index + 1))])
                        res.appendleft(dic[(10 ** index)])
                    else:
                        for i in range(6, rem + 1):
                            res.appendleft(dic[(10 ** index)])  
                        res.appendleft(dic[(10 ** index) * 5]) 
                    
            
            index += 1
            num //= 10
        
        return "".join(res)
            
            
            