class Solution:
    
    def areEqualSigns(self, first, second):
        return (first > 0 and second > 0) or (first < 0 and second < 0) or (first < 0 and second > 0)
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not len(stack) or self.areEqualSigns(stack[-1], asteroid):
                stack.append(asteroid)
            else:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                else:           
                    should_add = False
                    
                    while len(stack) and not self.areEqualSigns(stack[-1], asteroid):
                        if abs(stack[-1]) == abs(asteroid):
                            stack.pop()
                            should_add = False
                            break
                        elif abs(asteroid) > abs(stack[-1]):
                            should_add = True
                            stack.pop()
                        else:
                            should_add = False
                            break
                    
                    if should_add:
                        stack.append(asteroid)
                
        return stack