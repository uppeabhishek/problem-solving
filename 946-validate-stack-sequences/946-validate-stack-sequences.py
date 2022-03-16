class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        
        while i < len(pushed):
            if not len(stack):
                stack.append(pushed[i])
                i+=1
            else:
                if stack[-1] == popped[j]:
                    stack.pop()
                    j+=1
                else:
                    stack.append(pushed[i])
                    i+=1
        
        while j < len(popped):
            if stack[-1] != popped[j]:
                break
            else:
                stack.pop()
                j+=1
            
        return not len(stack)