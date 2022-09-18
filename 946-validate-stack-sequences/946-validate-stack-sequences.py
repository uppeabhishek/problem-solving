class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        
        i, j, n = 0, 0, len(pushed)
        
        while i < n:
            stack.append(pushed[i])
            
            if popped[j] == stack[-1]:
                while len(stack) and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
            
            i += 1
        
        while j < n:
            if popped[j] == stack[-1]:
                stack.pop()
                j += 1
            else:
                return False
        
        return True
        