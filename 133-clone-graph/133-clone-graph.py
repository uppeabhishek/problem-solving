"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def cloneGraphHelper(self, node):
        visited = {}
                
        queue = deque([node])

        visited[node] = Node(node.val)
        

        while queue:
            top = queue.popleft()

            for neighbor in top.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                    
                visited[top].neighbors.append(visited[neighbor])

        return visited[node]
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        return self.cloneGraphHelper(node)