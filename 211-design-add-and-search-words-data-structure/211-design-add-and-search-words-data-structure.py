from collections import defaultdict


class Node:
    def __init__(self, end=False):
        self.children = defaultdict(Node)
        self.end = end


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        temp = self.root

        for w in word:
            if w not in temp.children:
                temp.children[w] = Node()

            temp = temp.children[w]

        temp.end = True

    def searchHelper(self, root, word, i):

        if i == len(word):
            return root.end

        w = word[i]

        if w != '.':
            if w not in root.children:
                return False
            if self.searchHelper(root.children[w], word, i + 1):
                return True
        else:
            for key in root.children.keys():
                if self.searchHelper(root.children[key], word, i + 1):
                    return True

        return False

    def search(self, word: str) -> bool:
        temp = self.root
        return self.searchHelper(temp, word, 0)