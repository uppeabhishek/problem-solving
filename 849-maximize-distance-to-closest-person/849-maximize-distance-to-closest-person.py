class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        ones = []
        
        for i, seat in enumerate(seats):
            if seat == 1:
                ones.append(i)
                
        index = 0
        result = 0
                
        first, second = None, None
        
        for i, seat in enumerate(seats):
            if seat == 0:
                if first is None:
                    result += 1  
                else:
                    if i - first < second - i:
                        result = max(result, i - first)
                    else:
                        result = max(result, second - i)
            else:
                first = ones[index]
                second = ones[index + 1] if index + 1 < len(ones) else sys.maxsize
                index += 1
                
        return result