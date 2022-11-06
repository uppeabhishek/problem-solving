class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        dictionary = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        
        current, result = [], []
        
        def helper(j):
            
            nonlocal current, result
            
            if j == len(digits):
                if len(current):
                    result.append("".join(current))
                return
            
            digit = dictionary[int(digits[j])]
            
            for i in range(len(digit)):
                current.append(digit[i])
                helper(j + 1)
                current.pop()
                
            
        helper(0)
        return result
        