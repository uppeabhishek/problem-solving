class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        i = 0
        
        while i < len(s):
                        
            current = ""
            
            while s[i].isdigit():
                current += s[i]
                i += 1
                                    
            if current:
                stack.append(current)
            
            current = ""
                  
            if s[i] == "[":
                i += 1
                continue
                
            if s[i] != "]":
                stack.append(s[i])
                i += 1
            else:
                                
                queue = deque([])
                                
                while not stack[-1].isdigit():
                    queue.appendleft(stack.pop())
                
                top = stack.pop()
                
                current = "".join(queue) * int(top)
                
                stack.append(current)
                            
                i += 1
            
        return "".join(stack)
                
            