class LRUCache:

    def __init__(self, capacity: int):
        self.ordereddict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
                
        value = None
        
        if key in self.ordereddict:
            value = self.ordereddict[key]
        
        if value is None:
            return -1
        
        del self.ordereddict[key]
        self.ordereddict[key] = value
        
        return value
        

    def put(self, key: int, value: int) -> None:
        
        if len(self.ordereddict) == self.capacity and key not in self.ordereddict:
            self.ordereddict.popitem(last = False)
            
        if key not in self.ordereddict:
            self.ordereddict[key] = value
        else:
            del self.ordereddict[key]
            self.ordereddict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)