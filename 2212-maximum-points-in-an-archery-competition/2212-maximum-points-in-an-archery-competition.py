from copy import copy

class Solution:
    def __init__(self):
        self.max_val = -1
        self.cnt = 0
        self.max_result = [0] * 12
        self.current_result = [0] * 12

    def helper(self, points, numArrows, aliceArrows, index):
        self.cnt+=1
        if numArrows == 0 or index < 0:
            if points > self.max_val:
                self.max_val = points
                self.max_result = copy(self.current_result)
            return points

        if numArrows > aliceArrows[index]:
            # pick the arrow
            prev = self.current_result[index]        
            
            self.current_result[index] = numArrows if index == 0 else aliceArrows[index] + 1
            pick = self.helper(points + index, numArrows - aliceArrows[index] - 1, aliceArrows, index - 1)
            
            # backtrack
            self.current_result[index] = prev

            # dont pick the arrow
            dont_pick = self.helper(points, numArrows, aliceArrows, index - 1)
            return max(pick, dont_pick)
            
        return self.helper(points, numArrows, aliceArrows, index - 1)

    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.helper(0, numArrows, aliceArrows, 11)
        self.max_result[0]+= numArrows - sum(self.max_result) 
        return self.max_result
        