class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        dictionary = defaultdict(int)
        stack = []
        prev = None
        
        for log in logs:
            a, b, c = log.split(":")
            
            a, c = int(a), int(c)
            
            current = (a, b, c)
            
            if prev is None:
                stack.append(current)
            else:
                if b == 'end':
                    stack.pop()
                    if prev[1] == 'start':
                        dictionary[a] += c - prev[2] + 1
                    else:
                        dictionary[a] += c - prev[2]
                else:
                    if len(stack):                        
                        if prev[1] == 'end':
                            diff = c - prev[2] - 1   
                        else:
                            diff = c - prev[2]
                            
                        dictionary[stack[-1][0]] += diff                        
                    
                    stack.append(current)
            
            prev = current
            
        result = [0] * n
        
        for key, value in dictionary.items():
            result[key] = value
        
        return result
        