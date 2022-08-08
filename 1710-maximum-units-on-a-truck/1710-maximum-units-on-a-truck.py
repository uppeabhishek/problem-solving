class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda k: (k[1]), reverse = True)
        result = 0
                
        for box in boxTypes:
            if box[0] > truckSize:
                result += truckSize * box[1]
                truckSize = 0
                break
                
            result += box[0] * box[1]
            truckSize -= box[0]
            
        return result        