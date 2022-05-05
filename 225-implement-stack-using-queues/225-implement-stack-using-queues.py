class MyStack:

    def __init__(self):
        self.deque = deque([])

    def push(self, x: int) -> None:
        self.deque.append(x)
        if len(self.deque) > 1:
            l = len(self.deque) - 1
            i = 0
            while i < l:
                self.deque.append(self.deque.popleft())
                i += 1
            
    def pop(self) -> int:
        return self.deque.popleft()

    def top(self) -> int:
        return self.deque[0]

    def empty(self) -> bool:
        return len(self.deque) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()