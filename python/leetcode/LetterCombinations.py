from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        result = []
        tempResult = []

        def recursion(i):

            if i == len(digits):
                result.append("".join(tempResult))
                return

            for i1 in range(len(dic[digits[i]])):
                tempResult.append(dic[digits[i]][i1])
                recursion(i + 1)
                tempResult.pop()

        recursion(0)

        return result


s = Solution()
s.letterCombinations("234")
