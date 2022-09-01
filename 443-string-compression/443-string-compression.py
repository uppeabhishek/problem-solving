class Solution:   
    def compress(self, chars: List[str]) -> int:
        
        i = 0
        j = 0
        
        while i < len(chars):
            
            cnt = 1
            
            while i < len(chars) - 1 and chars[i] == chars[i + 1]:
                i = i + 1
                cnt += 1
            

            chars[j] = chars[i]
            
            j += 1
            
            start, end = j, j
            
            if cnt > 1:
                while cnt:
                    chars[j] = str(cnt % 10)
                    j += 1    
                    cnt = cnt // 10
                
                end = j - 1
                
                while start < end:
                    temp = chars[start]
                    chars[start] = chars[end]
                    chars[end] = temp
                    
                    start += 1
                    end -= 1
                
            i += 1
        
        return j
            
        
            