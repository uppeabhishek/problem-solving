class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        paths = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]

        def BFS():
            queue = deque([(0, 0, 0)])

            end_queue = deque([(x, y, 0)])

            visited1 = {(0, 0): 0}

            visited2 = {(x, y): 0}

            while len(queue):

                x1, y1, distance = queue.popleft()

                x2, y2, distance = end_queue.popleft()

                if (x1, y1) in visited2:
                    return distance + visited2[(x1, y1)]

                if (x2, y2) in visited1:
                    return distance + visited1[(x2, y2)]

                for path in paths:

                    x3, y3 = x1 + path[0], y1 + path[1]

                    if (x3, y3) not in visited1:
                        queue.append((x3, y3, distance + 1))
                        visited1[(x3, y3)] = distance + 1

                    x4, y4 = x2 + path[0], y2 + path[1]

                    if (x4, y4) not in visited2:
                        end_queue.append((x4, y4, distance + 1))
                        visited2[(x4, y4)] = distance + 1
        
        return BFS()