from leetcode.TreeNode import TreeNode


class Solution:

    def helper(self, root):
        if root is None:
            return

        self.helper(root.left)

        if self.result is None:
            self.result = root
            self.current_result = self.result
        else:
            self.current_result.right = root
            self.current_result = self.current_result.right
            self.current_result.left = None

        self.helper(root.right)

        return self.result

    def increasingBST(self, root):
        self.result = None
        self.current_result = None
        self.helper(root)
        return self.result


s = Solution()
# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(7)

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.left.left.left = TreeNode(1)
# root.right = TreeNode(6)
# root.right.right = TreeNode(8)
# root.right.right.left = TreeNode(7)
# root.right.right.right = TreeNode(9)

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(1)

s.increasingBST(root)
