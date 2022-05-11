class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = 5
        res = [1] * vowels
        for i in range(1, n):
            for j in range(1, vowels):
                res[j] = res[j] + res[j - 1]
            
        return sum(res)