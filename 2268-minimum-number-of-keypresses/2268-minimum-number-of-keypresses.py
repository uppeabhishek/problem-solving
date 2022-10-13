class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = Counter(s)
        counter = counter.most_common()    
        current_cnt = 0
        result = 0
        
        for i, ele in enumerate(counter):
            if i % 9 == 0:
                current_cnt += 1               
            result += ele[1] * current_cnt
            
        return result
            
        
        
        
            
            
            