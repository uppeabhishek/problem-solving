class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.k = k
        self.size = 0
        self.index = -1
        self.delete_index = 0

    def enQueue(self, value: int) -> bool:        
        if self.isFull():
            return False
        
        queue = self.queue
        self.index = (self.index + 1) % self.k
        self.queue[self.index] = value
        self.size += 1
        return True
            
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        queue = self.queue
        self.queue[self.delete_index] = None
        self.size -= 1
        self.delete_index = (self.delete_index + 1) % self.k
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.delete_index]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.index]
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()