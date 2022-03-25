from functools import cmp_to_key

def compare(a, b):
    first = a[0] - a[1]
    second = b[0] - b[1]
    if first < second:
        return -1
    elif first > second:
        return 1
    return 0
    
class Solution:
        
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = cmp_to_key(compare))
        return sum([cost[0] if i < len(costs) // 2 else cost[1] for i, cost in enumerate(costs)])
        