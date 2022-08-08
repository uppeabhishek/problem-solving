from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        
        heap = []
        
        for c in counter:
            heappush(heap, (-counter[c], c))    
        
        result = []
        
        while len(heap):
            top1 = heappop(heap)
            if not len(heap):
                if top1[0] != -1:
                    return ""
                result.append(top1[1])
            else:
                top2 = heappop(heap)
                
                result.append(top1[1])
                result.append(top2[1])
                
                
                top1 = (top1[0] + 1, top1[1])
                top2 = (top2[0] + 1, top2[1])
                                
                if top1[0] != 0:
                    heappush(heap, top1)
                
                if top2[0] != 0:
                    heappush(heap, top2)
                
            
        return "".join(result)
            
                
            
            
    