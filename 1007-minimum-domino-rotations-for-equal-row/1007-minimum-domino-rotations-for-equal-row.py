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
        dic = defaultdict(int)
        for i in range(len(tops)):
            dic[tops[i]]+=1
            dic[bottoms[i]]+=1
        
        should_check = []
        for key, value in dic.items():
            if value >= len(tops):
                should_check.append(key)    
        
        result = sys.maxsize

        for ele in should_check:
            shouldCount, cnt = self.getMinCount(tops, bottoms, ele)
            if shouldCount:
                result = min(result, cnt)
            
            shouldCount, cnt = self.getMinCount(bottoms, tops, ele)
            if shouldCount:
                result = min(result, cnt)
        
        return -1 if result == sys.maxsize else result          
    