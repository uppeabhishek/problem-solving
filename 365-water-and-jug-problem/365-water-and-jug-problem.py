class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while len(queue):
            
            
            a, b = queue.popleft()
                        
            if a == targetCapacity or b == targetCapacity or a + b == targetCapacity:
                return True
            
            next_states = set()
            
            # fill
            next_states.add((jug1Capacity, b))
            next_states.add((a, jug2Capacity))
            
            # empty
            if a > 0 and b > 0:
                next_states.add((0, b))
                next_states.add((a, 0))
                
            # pour
            if a < jug1Capacity or b < jug2Capacity:
                
                # a to b
                b1 = jug2Capacity - b
                
                if a <= b1:
                    next_states.add((0, b + a))
                else:
                    next_states.add((a - b1, jug2Capacity))
                    
                # b to a
                a1 = jug1Capacity - a
                
                if b <= a1:
                    next_states.add((a + b, 0))
                else:
                    next_states.add((jug1Capacity, b - a1))
                        
            for next_state in next_states:
                if next_state not in visited:
                    queue.append(next_state)
                    visited.add(next_state)
        
        return False