class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def bsearch(self, arr, key):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if key < arr[mid][0]:
                right = mid - 1
            elif key > arr[mid][0]:
                left = mid + 1
            else:
                return arr[mid][1]
        
        if right < 0:
            return ""
        
        return arr[right][1]
         
    def get(self, key: str, timestamp: int) -> str:
        if not len(self.dictionary[key]):
            return ""
        
        return self.bsearch(self.dictionary[key], timestamp)
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)