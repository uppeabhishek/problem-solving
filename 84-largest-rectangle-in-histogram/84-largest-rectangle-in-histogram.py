class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        
        max_area = 0
        
        n = len(heights)
        
        for i, height in enumerate(heights):
            
            current = (i, heights[i])
            
            if not len(stack):
                stack.append(current)
            else:
                if heights[i] > stack[-1][1]:
                    stack.append(current)
                else:
                    prev_i = i
                    while len(stack) and stack[-1][1] > heights[i]:
                        max_area = max(max_area, stack[-1][1] * (i - stack[-1][0]))
                        prev_i = stack[-1][0]
                        stack.pop()
                                        
                    stack.append((prev_i, heights[i]))
                                                            
        while len(stack):
            index, val = stack.pop()
            max_area = max(max_area, (n - index) * val)
        
        return max_area
        