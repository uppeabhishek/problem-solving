class Node:
    def __init__(self, end=False):
        self.children = defaultdict(Node)
        self.end = end


class Solution:

    def __init__(self):
        self.cnt = 0
        self.root = Node()

    def insertIntoTrie(self, product):
        temp = self.root
        for p in product:
            if p not in temp.children:
                temp.children[p] = Node()
            temp = temp.children[p]
        temp.end = True

    def searchDFS(self, currentWord, root, result):
        if root.end:
            self.cnt += 1
            if self.cnt <= 3:
                result.append(currentWord)
            else:
                return

        for key, value in root.children.items():
            self.searchDFS(currentWord + key, value, result)

    def search(self, word):
        present = True
        root = self.root
        currentWord = ""
        for w in word:
            if w not in root.children:
                present = False
                break
            currentWord += w
            root = root.children[w]

        if not present:
            return []

        self.cnt = 0
        result = []
        self.searchDFS(currentWord, root, result)
        return result

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        for p in products:
            self.insertIntoTrie(p)

        result = []

        for i in range(len(searchWord)):
            result.append(self.search(searchWord[0: i + 1]))

        return result