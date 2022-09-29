"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = defaultdict(list)
        
        def helper(node):
            
            if node is None:
                return None
            
            if node in visited:
                return visited[node]
        
            new_node = Node(node.val)
            
            visited[node] = new_node
            
            new_node.neighbors = [helper(n) for n in node.neighbors]
            
            return new_node
    
        return helper(node)