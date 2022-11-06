# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

from python.leetcode.TreeNode import TreeNode


class Codec:

    def __init__(self):
        self.null = 'null'

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return ""

        result = []

        queue = deque([root])

        while len(queue):
            top = queue.popleft()

            if top:
                result.append(top.val)
            else:
                result.append(self.null)

            if top:
                queue.append(top.left)
                queue.append(top.right)

        return " ".join(list(map(str, result)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        array = data.split(" ")

        root = None
        tempRoot = None

        queue = deque([(tempRoot, 0, None)])

        while len(queue):

            tempRoot, index, isLeft = queue.popleft()

            if array[index] == self.null:
                newNode = None
            else:
                newNode = TreeNode(array[index])

            if root is None:
                tempRoot = newNode
                root = tempRoot
            else:
                if isLeft:
                    tempRoot.left = newNode
                else:
                    tempRoot.right = newNode

            last_index = index
            if len(queue):
                last_index = queue[-1][1]

            left = last_index + 1
            right = last_index + 2

            if left < len(array) and newNode:
                queue.append((newNode, left, True))

            if right < len(array) and newNode:
                queue.append((newNode, right, False))

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

s = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)
root.right.right = TreeNode(5)
s.deserialize(s.serialize(root))
