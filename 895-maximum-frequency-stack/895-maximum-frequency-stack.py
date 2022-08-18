class FreqStack:

    def __init__(self):
        self.stacks = []
        self.dict = defaultdict(int)
        
    def push(self, val: int) -> None:
          
        self.dict[val] += 1
                                
        if len(self.stacks) < self.dict[val]:
            self.stacks.append([])
        
        self.stacks[self.dict[val] - 1].append(val)
        

    def pop(self) -> int:
        last_stack = self.stacks[-1]
        
        last_ele = last_stack.pop()
        
        if not len(last_stack):
            self.stacks.pop()
        
        self.dict[last_ele] -= 1
        
        return last_ele

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()