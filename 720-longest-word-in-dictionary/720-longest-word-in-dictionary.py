from collections import defaultdict
from typing import List


class Node:
    def __init__(self, end=False):
        self.children = defaultdict(Node)
        self.end = end
        self.avoid_path = False


class Solution:

    def addToTrie(self, word, root):

        total_cnt = 0
        is_new_char = False
        new_cnt = 0
        current = ""
        temp_root = root
        should_avoid_path = False
        first_new_index = None

        for i, w in enumerate(word):

            if w not in temp_root.children:

                if first_new_index is None:
                    first_new_index = i

                temp_root.children[w] = Node()
                new_cnt += 1
                if i == len(word) - 1:
                    if new_cnt == 1 and not should_avoid_path:
                        is_new_char = True

            current += word[i]
            total_cnt += 1
            temp_root = temp_root.children[w]

            if temp_root.avoid_path:
                should_avoid_path = temp_root.avoid_path

        temp_root.end = True

        if new_cnt > 1:
            temp_root = root
            for i, w in enumerate(word):
                temp_root = temp_root.children[w]
                if i >= first_new_index:
                    temp_root.avoid_path = True

        return is_new_char, word

    def longestWord(self, words: List[str]) -> str:

        words = list(set(words))

        words.sort()

        root = Node()
        result_cnt, result = 0, ""

        for word in words:
            is_new_char, word = self.addToTrie(word, root)
            word_len = len(word)

            if is_new_char:
                if word_len > result_cnt:
                    result = word
                else:
                    result = min(result, word)

                result_cnt = max(result_cnt, word_len)

        return result