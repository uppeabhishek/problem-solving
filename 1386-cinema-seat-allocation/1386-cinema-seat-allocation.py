class Solution:
    
    def checkIfFree(self, allocated, seats, index):
        free = True
        for ele in seats:
            if ele in allocated[index]:
                free = False
                break
    
        return free
    
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        allocated = defaultdict(set)
                
        for start, end in reservedSeats:
            allocated[start].add(end)
        
        result = 0
        
        first, second, third = [2, 3, 4, 5], [4, 5, 6, 7], [6, 7, 8, 9]
        
        cnt = 0
        
        for key in allocated.keys():
            cnt += 1
            if self.checkIfFree(allocated, first, key):
                result += 1
                if self.checkIfFree(allocated, third, key):
                    result += 1 
            else:
                if self.checkIfFree(allocated, second, key):
                    result += 1
                elif self.checkIfFree(allocated, third, key):
                    result += 1 
        
        return result + (n - cnt) * 2
                
                
                
            
            
        