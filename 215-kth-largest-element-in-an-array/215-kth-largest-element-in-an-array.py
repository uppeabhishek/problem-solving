from heapq import heappush, heappushpop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            else:
                if num > heap[0]:
                    heappushpop(heap, num)
            
    
        return heap[0]