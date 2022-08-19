# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        
        def infixToPostfix(s):
            precedence = {'+': 1, '-': 1, '*': 2, "/": 2, '(': 3, ')': 3}
            stack = []
            result_stack = []

            i = 0

            while i < len(s):
                c = s[i]

                if c == ' ':
                    i += 1
                    continue

                if c == "(":
                    stack.append(c)
                    i += 1
                    continue

                if c == ")":

                    temp = deque([])

                    while stack[-1] != "(":
                        temp.appendleft(stack.pop())

                    stack.pop()

                    while len(temp):
                        result_stack.append(temp.pop())

                    i += 1
                    continue


                if c not in precedence:
                    temp = []
                    while i < len(s) and s[i] not in precedence and s[i] != ' ':
                        temp.append(s[i])
                        i += 1

                    result_stack.append("".join(temp) + " ")

                else:
                    if not len(stack) or precedence[c] > precedence[stack[-1]]:
                        stack.append(c)
                    else:
                        while len(stack) and stack[-1] != "(":
                            if precedence[c] <= precedence[stack[-1]]:
                                result_stack.append(stack.pop())
                            else:
                                break

                        stack.append(c)
                    i += 1


            while len(stack):
                result_stack.append(stack.pop())

            return "".join(result_stack)
    
    
        def helper():
            nonlocal s
            
            s = infixToPostfix(s)
                        
            chars = {'+', '-', '/', '*'}

            stack = []
            
            for p in s:
                if p not in chars:
                    if p != " ":
                        stack.append(Node(p))
                else:
                    right = stack.pop()
                    left = stack.pop()            
                    stack.append(Node(p, left, right))
            
            return stack[0]
    
        return helper()
    