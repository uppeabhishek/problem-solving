class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        queue = deque([])
        
        def addToQueue(ele):
            if not len(queue):
                queue.append(ele)
            else:
                if ele <= queue[-1]:
                    queue.append(ele)
                else:
                    while len(queue) and ele > queue[-1]:
                        queue.pop()
                    queue.append(ele)
        
        def helper():
            
            result = []
            
            for i in range(k):
                addToQueue(nums[i])
            
            result = [queue[0]]
            
            i = k
            prev_i = 0
            
            while i < len(nums):
                
                if nums[prev_i] == queue[0]:
                    queue.popleft()
                
                addToQueue(nums[i])
                
                result.append(queue[0])
                
                i += 1
                prev_i += 1
                    
                
            return result
    
        return helper()
            