class Solution:
    
    def getMinCount(self, top, bottom, current):
        cnt = 0
        shouldCount = True
        for i in range(len(top)):
            if top[i] == current:
                continue
            elif bottom[i] == current:
                cnt+=1
            else:
                shouldCount = False
                break
        
        return (shouldCount, cnt)
        
        
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result = sys.maxsize
        
        for i in range(1, 7):
            shouldCount, cnt = self.getMinCount(tops, bottoms, i)
            if shouldCount:
                result = min(result, cnt)
            
            shouldCount, cnt = self.getMinCount(bottoms, tops, i)
            if shouldCount:
                result = min(result, cnt)
        
        return -1 if result == sys.maxsize else result