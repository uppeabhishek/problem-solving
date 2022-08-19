import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeNode(Node):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.chars = {'+', '-', '/', '*'}
    
    def compute(self, left, right, val):
        left, right = int(left), int(right)
        if val == "+":
            return left + right
        if val == "-":
            return left - right
        if val == "*":
            return left * right
        return left // right
        
    def helper(self):
        
        if self is None:
            return 0
        
        if self.left is None and self.right is None:
            return self.val
        
        left, right = self.left.val, self.right.val
                
        if left not in self.chars and right not in self.chars:
            return self.compute(left, right, self.val)
        
        left = self.left.helper()
        right = self.right.helper()
        
        return self.compute(left, right, self.val)
        
        
    def evaluate(self):
        return self.helper()
    
class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        
        chars = {'+', '-', '/', '*'}
        
        stack = []

        for p in postfix:
            if p not in chars:
                stack.append(TreeNode(p))
            else:
                right = stack.pop()
                left = stack.pop()
                
                stack.append(TreeNode(p, left, right))
        
        return stack[0]
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        