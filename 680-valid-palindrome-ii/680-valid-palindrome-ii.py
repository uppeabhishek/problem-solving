class Solution:
    def isPalindrome(self, s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if i + 1 == j:
                    return True
                if s[i + 1] == s[j]:
                    if self.isPalindrome(s, i + 1, j):
                        return True
                if s[i] == s[j - 1]:
                    if self.isPalindrome(s, i, j - 1):
                        return True
                return False
            else:
                i += 1
                j -= 1

        return True