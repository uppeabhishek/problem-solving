from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        visited = set()
        new_visited = dict()

        queue = deque()

        actual_result = Node(node.val)
        result = actual_result

        queue.append((node, result))
        visited.add(node)
        new_visited[result.val] = result

        while len(queue):
            top, result = queue.popleft()
            for ele in top.neighbors:
                if ele not in visited:
                    new_node = Node(ele.val)
                    result.neighbors.append(new_node)
                    queue.append((ele, new_node))
                    visited.add(ele)
                    new_visited[new_node.val] = new_node
                else:
                    result.neighbors.append(new_visited[ele.val])
        return result


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
