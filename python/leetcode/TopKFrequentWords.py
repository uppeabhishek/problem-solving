from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Node:
    def __init__(self, val, char):
        self.val = val
        self.char = char

    def __lt__(self, other):
        if self.val != other.val:
            return self.val < other.val
        return self.char > other.char

    def __eq__(self, other):
        return self.char > other.char


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        dic = defaultdict(int)

        for word in words:
            dic[word] += 1

        heap = []

        for key, value in dic.items():

            val = Node(value, key)

            if len(heap) < k:
                heappush(heap, val)
            else:
                if value > heap[0].val:
                    heappop(heap)
                    heappush(heap, val)
                elif value == heap[0].val:
                    if key < heap[0].char:
                        heappop(heap)
                        heappush(heap, val)

        for h in heap:
            print(h.val, h.char)

        print()


s = Solution()
# s.topKFrequent(["a", "a", "a", "b", "b", "c", "c", "z", "z", "y", "y", "d", "d", "e", "e", "e"], 5)
s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1)
