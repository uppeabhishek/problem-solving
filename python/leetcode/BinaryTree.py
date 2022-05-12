# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional

from leetcode.TreeNode import TreeNode


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic = defaultdict(list)
        for description in descriptions:
            dic[description[0]].append((description[1], description[2]))

        dic_keys = set(dic.keys())

        for keys, values in dic.items():
            for value in values:
                dic_keys.discard(value[0])

        first = next(iter(dic_keys))

        root_node = TreeNode(first)
        queue = deque([root_node])

        while len(queue):
            top = queue.pop()
            if top.val in dic:
                values = dic[top.val]
                if len(values) == 1:
                    node = TreeNode(values[0][0])
                    if values[0][1] == 1:
                        top.left = node
                    else:
                        top.right = node
                    queue.append(node)
                else:
                    lnode = TreeNode(values[0][0])
                    rnode = TreeNode(values[1][0])
                    if values[0][1] == 0:
                        lnode = TreeNode(values[1][0])
                        rnode = TreeNode(values[0][0])
                    top.left = lnode
                    top.right = rnode
                    queue.append(lnode)
                    queue.append(rnode)

        return root_node


s = Solution()
s.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
s.createBinaryTree([[1, 2, 1], [2, 3, 0], [3, 4, 1]])
