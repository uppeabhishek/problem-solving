class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if x <= arr[0]:
            return arr[0 : k]
        
        if x >= arr[-1]:
            return arr[len(arr) - k: ]
        
        def bsearch(low, high):

            if low > high:
                if abs(arr[high] - x) <= abs(arr[low] - x):
                    return high
                return low
            
            mid = (low + high) >> 1
            
            if arr[mid] == x:
                return mid
            elif x < arr[mid]:
                return bsearch(low, mid - 1)
            else:
                return bsearch(mid + 1, high)
        
        index = bsearch(0, len(arr) - 1)
        
        result = []
        
        low, high = index - 1, index + 1
                
        while k > 0:
            
            result.append(arr[index])
            
            k -= 1
            
            if low >= 0 and high < len(arr):
                if abs(x - arr[low]) <= abs(x - arr[high]):
                    index = low
                    low -= 1
                else:
                    index = high
                    high += 1
            elif low >= 0:
                index = low
                low -= 1
            else:
                index = high
                high += 1
            
        return sorted(result)
            
        
            