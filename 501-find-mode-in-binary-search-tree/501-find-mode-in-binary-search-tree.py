# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
           
    def max_inorder(self, root, val):
        if root is None:
            return
        
        self.max_inorder(root.left, val)
        
        if self.cnt == 0:
            self.cnt = 1
            self.val = root.val
        else:
            if root.val == self.val:
                self.cnt+=1
            else:                
                if self.cnt == val:
                    self.result.append(self.val)
                
                self.cnt = 1
                self.val = root.val
                
        
        self.max_inorder(root.right, val)
        
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        
        if self.cnt == 0:
            self.cnt = 1
            self.val = root.val
        else:
            if root.val == self.val:
                self.cnt+=1
            else:
                if self.cnt > self.max_cnt:
                    self.max_cnt = self.cnt
                    self.max_val = self.val
                
                self.cnt = 1
                self.val = root.val   
        
        self.inorder(root.right)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.val, self.max_val, self.cnt, self.max_cnt = 0, 0, 0, 0
        
        actual_root = root
        
        self.inorder(root)
        
        if self.cnt > self.max_cnt:
            self.max_cnt = self.cnt
            self.max_val = self.val
        
        self.result = []
        
        self.val, self.cnt = 0, 0
        
        self.max_inorder(root, self.max_cnt)
                
        if self.cnt == self.max_cnt:
            if len(self.result) == 0 or self.result[-1] != self.val:
                self.result.append(self.val)
        
        return self.result
    