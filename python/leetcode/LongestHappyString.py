from heapq import heapify, heappush, heappop


class Solution:

    def addToHeap(self, heap, val):
        if val[0]:
            heappush(heap, val)

    def addToResult(self, result, heap_ele):
        heap_cnt, heap_val = heap_ele
        heap_cnt = abs(heap_cnt)

        i = 0
        while heap_cnt and i < 2:
            result.append(heap_val)
            heap_cnt -= 1
            i += 1

        return heap_cnt

    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapify(heap)

        result = []

        while len(heap):

            top = heappop(heap)
            top_cnt, top_val = top

            top_cnt = top_cnt * - 1

            if len(result):
                if result[-1] == top_val:
                    if not len(heap):
                        break
                    else:
                        second_top = heappop(heap)
                        second_top_cnt, second_top_val = second_top

                        second_top_cnt = self.addToResult(result, second_top)

                        self.addToHeap(heap, (-second_top_cnt, second_top_val))
                        self.addToHeap(heap, (-top_cnt, top_val))

                else:
                    top_cnt = self.addToResult(result, top)
                    self.addToHeap(heap, (-top_cnt, top_val))
            else:
                top_cnt = self.addToResult(result, top)
                self.addToHeap(heap, (-top_cnt, top_val))


s = Solution()
s.longestDiverseString(3, 3, 3)
