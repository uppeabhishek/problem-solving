from heapq import heappop, heappush
class StockPrice:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.current_val = None
        self.timestamp = 0
        self.dict = defaultdict(int)

    def update(self, timestamp: int, price: int) -> None:
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

        self.dict[timestamp] = price
        
        if timestamp >= self.timestamp:
            self.current_val = price
            self.timestamp = timestamp

    def current(self) -> int:
        return self.current_val

    def maximum(self) -> int:
        
        while True:
            price, timestamp = self.max_heap[0]
            price = abs(price)
            
            if price == self.dict[timestamp]:
                return price
            
            heappop(self.max_heap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.min_heap[0]
            
            if price == self.dict[timestamp]:
                return price
            
            heappop(self.min_heap)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()