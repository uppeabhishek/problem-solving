class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dis = math.inf
        ind = -1
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                current = abs(point[0] - x) + abs(point[1] - y)
                if current < dis:
                    dis = current
                    ind = i
                
        return ind if dis is not math.inf else -1