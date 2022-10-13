from collections import defaultdict


class Solution:

    def bsearch(self, array, value):

        l, r = 0, len(array) - 1

        while l < r:

            m = (l + r) // 2

            if array[m] == value:
                return array[m]
            elif value < array[m]:
                r = m
            else:
                l = m + 1

        if l == len(array):
            return -1

        return array[l]

    def isSubsequence(self, dictionary, word):

        current_index = -1

        for c in word:
            
            if c not in dictionary:
                return False

            index = self.bsearch(dictionary[c], current_index)

            if index == -1 or index < current_index:
                return False

            current_index = index + 1

        return True

    def numMatchingSubseq(self, s, words):

        dictionary = defaultdict(list)

        for i, c in enumerate(s):
            dictionary[c].append(i)

        result = 0

        for word in words:
            if self.isSubsequence(dictionary, word):
                result += 1

        return result