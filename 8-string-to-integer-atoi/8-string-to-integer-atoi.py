class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        def cleanString(s):
            
            new_s = ''
            
            result = 0
            
            s = s.strip()

            positive = True

            for i in range(len(s)):
                c = s[i]

                if i == 0:
                    if c == '-':
                        positive = False
                    elif c == '+':
                        continue
                    else:
                        if c.isdigit():
                            new_s += c
                        else:
                            break
                else:
                    if c.isdigit():
                        new_s += c
                    else:
                        break
        
            return new_s, positive
        
        
        max_val = 2 ** 31
        
        new_s, positive = cleanString(s)
        result = 0
        index = 0
        
        while index < len(new_s):
            result = result * 10 + int(new_s[index])
            
            if positive:
                if result > max_val - 1:
                    return max_val - 1
            else:
                if result > max_val:
                    return -max_val
            
            index += 1
        
        if not positive:
            return -1 * result
        
        return result