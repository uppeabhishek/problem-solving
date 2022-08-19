class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        prefix, candles = [0] * len(s), []
        
        result = []

        def addPrefixCandles():        
            for i, c in enumerate(s):
                if c == "|":
                    prefix[i] = prefix[i - 1] if i - 1 > -1 else 0
                    candles.append(i)
                else:
                    if len(candles):
                        prefix[i] = prefix[i - 1] + 1
        
        def bsearch(low, high, key, lesser):
            
            if low > high:                
                if lesser:
                    return candles[max(high, 0)]
                
                return candles[min(low, len(candles) - 1)]
                
            mid = (low + high) // 2
            
            if candles[mid] == key:
                return candles[mid]
            elif key < candles[mid]:
                return bsearch(low, mid - 1, key, lesser)
            return bsearch(mid + 1, high, key, lesser)
            
        def queryHelper():
            for query in queries:
                
                if not len(candles):
                    result.append(0)
                    continue
                
                low, high = 0, len(candles) - 1
                
                
                first = bsearch(low, high, query[0], False)
                second = bsearch(low, high, query[1], True)
                
                if first < second:
                    result.append(prefix[second] - prefix[first])
                else:
                    result.append(0)
        
        addPrefixCandles()
        queryHelper()
        
        return result