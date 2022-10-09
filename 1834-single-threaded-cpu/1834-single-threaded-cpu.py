class Node:
    
    def __init__(self, processing_time, enque_time, index):
        self.processing_time = processing_time
        self.enque_time = enque_time
        self.index = index
    
    def __lt__(self, other):
        if self.processing_time == other.processing_time:
            return self.index < other.index
        
        return self.processing_time < other.processing_time
    
class Solution:
        
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort()
                
        heap = []
        idle_time = tasks[0][0]
        
        result = []
            
        index = 0
        
        while index < len(tasks):
                        
            didEnter = False
            
            while index < len(tasks) and tasks[index][0] <= idle_time:
                i, j, k = tasks[index]
                heappush(heap, Node(j, i, k))
                index += 1
                didEnter = True
            
            if len(heap):
                node = heappop(heap)
                idle_time = idle_time + node.processing_time

                result.append(node.index)
                didEnter = True
            
            if not didEnter:
                idle_time = tasks[index][0]
            
        while len(heap):
            node = heappop(heap)
            result.append(node.index)
        
        return result
                