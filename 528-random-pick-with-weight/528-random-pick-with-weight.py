import random

class Solution:

    def __init__(self, w: List[int]):
        self.list = [(index, ele) for index, ele in enumerate(w)]
        self.weights = tuple([ele[1] / sum(w) for ele in self.list])       

    def pickIndex(self) -> int:
        res = random.choices(self.list, weights=self.weights, k=1)
        return res[0][0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()