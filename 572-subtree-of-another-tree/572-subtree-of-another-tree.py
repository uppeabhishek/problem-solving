# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def treeToString(self, root, result):
        if root is None:
            result.append("#")
            return

        result.append("$" + str(root.val))
        
        self.treeToString(root.left, result)
        self.treeToString(root.right, result)
        
        
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootResult = []
        subRootResult = []
        
        self.treeToString(root, rootResult)
        self.treeToString(subRoot, subRootResult)
        
        subRootResult = "".join(subRootResult)
        rootResult = "".join(rootResult)
                
        return subRootResult in rootResult
        
        