class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        
        result = [0] * n
        
        stack = []
        
        i = n - 1
        
        while i > -1:
            
            if not len(stack):
                stack.append(i)
            else:
                while len(stack) and temperatures[stack[-1]] <= temperatures[i]:
                    stack.pop()
                
                if len(stack):
                    result[i] = stack[-1] - i
                
                stack.append(i)
            
            i -= 1
            
        return result
            