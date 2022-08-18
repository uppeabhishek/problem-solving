class HitCounter:

    def __init__(self):
        self.queue = deque([])

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        
    def getHits(self, timestamp: int) -> int:
        i = 0
        elements_to_pop = 0
        result = 0
        
        while i < len(self.queue):
            if timestamp - self.queue[i] >= 300:
                elements_to_pop += 1
            else:
                result += 1
            
            i += 1
        
        i = 0
        
        while i < elements_to_pop:
            self.queue.popleft()
            i += 1
        
        return result
            

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)