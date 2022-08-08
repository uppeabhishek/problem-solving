from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


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
                visited[top].neighbors.append(neighbor)

        return visited[node]

    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.cloneGraphHelper(node)


if __name__ == "__main__":
    s = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    s.cloneGraph(node1)
