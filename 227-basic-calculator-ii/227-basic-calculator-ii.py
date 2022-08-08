class Solution:
    
    def infixToPostfix(self, s):
        precedence = {'+': 1, '-': 1, '*': 2, "/": 2}
        stack = []
        result_stack = []
        
        i = 0
        
        while i < len(s):
            c = s[i]
        
            if c == ' ':
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
                    while len(stack):
                        if precedence[c] <= precedence[stack[-1]]:
                            result_stack.append(stack.pop())
                        else:
                            break
                    stack.append(c)
                i += 1
        
        
        while len(stack):
            result_stack.append(stack.pop())
        
        return "".join(result_stack)
    
    
    def computeResult(self, first, second, operator):
        first, second = int(first), int(second)
        
        if operator == "+":
            return first + second
        
        if operator == "-":
            return first - second
        
        if operator == "*":
            return first * second
    
        return first // second
        
    def postfixEvaluation(self, s):
                
        stack = []
        
        operators = {'+', '-', '*', '/'}

        i = 0
        
        while i < len(s):
            c = s[i]
            
            if c in operators:
                second = stack.pop()
                first = stack.pop()
                stack.append(self.computeResult(first, second, c))
                i += 1
            else:
                temp = []
                while i < len(s) and s[i] != ' ':
                    temp.append(s[i])
                    i += 1
                i += 1
                stack.append("".join(temp))
                
        return stack[-1]
            
        
    def calculate(self, s: str) -> int:
        postfix = self.infixToPostfix(s)  
        return self.postfixEvaluation(postfix)