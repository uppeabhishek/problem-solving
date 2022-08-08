# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, postorder, inorder_dictionary, left, right):
        if left > right:
            return None

        index = inorder_dictionary[postorder[self.index]]
        root = TreeNode(postorder[self.index])

        self.index += 1

        root.right = self.helper(postorder, inorder_dictionary, index + 1, right)
        root.left = self.helper(postorder, inorder_dictionary, left, index - 1)

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        self.index = 0

        inorder_dictionary = collections.defaultdict(int)

        for i, ele in enumerate(inorder):
            inorder_dictionary[ele] = i

        postorder = postorder[::-1]
        return self.helper(postorder, inorder_dictionary, 0, len(postorder) - 1)