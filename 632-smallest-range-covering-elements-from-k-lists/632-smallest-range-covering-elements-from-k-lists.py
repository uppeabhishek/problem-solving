from heapq import heapify, heappush, heappop

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        min_heap, max_heap_val = [], -sys.maxsize
        
        for i in range(len(nums)):
            heappush(min_heap, (nums[i][0], i, 0))
            if nums[i][0] > max_heap_val:
                max_heap_val = nums[i][0]

        min_val = None
        max_val = max_heap_val
        current_range = sys.maxsize
        
        while True:
                        
            if max_heap_val - min_heap[0][0] < current_range:
                current_range = max_heap_val - min_heap[0][0]
                min_val = min_heap[0]
                max_val = max_heap_val
            
            i, j = min_heap[0][1], min_heap[0][2]
                        
            if j + 1 == len(nums[i]):
                break
            
            current = nums[i][j + 1]

            heappop(min_heap)
            heappush(min_heap, (current, i, j + 1))

            if current > max_heap_val:
                max_heap_val = current
                        
            
        return [min_val[0], max_val]