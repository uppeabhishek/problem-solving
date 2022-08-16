class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        if n == 0:
            return [0]
        
        if n == 1:
            return [0, 1]
        
        if n == 2:
            return [0, 1, 1]
        
        if n == 3:
            return [0, 1, 1, 2]
    
    
        cache = [1, 2]
        cnt = 3

        result = [0, 1, 1, 2]
        
        while cnt <= n:
                        
            new_cache = []
            
            for i in range(len(cache)):
                shouldBreak = False
                
                cnt += 1
                new_cache.append(cache[i] + 0)
                if cnt == n:
                    cnt += 1
                    break
                    
                cnt += 1
                new_cache.append(cache[i] + 1)
                if cnt == n:
                    cnt += 1
                    break
                
            cache = new_cache
            result += cache
                
        return result
        
        
                    
                    