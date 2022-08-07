class Node:
    def __init__(self, end=False):
        self.children = defaultdict(Node)
        self.end = end


class Solution:

    def __init__(self):
        self.root = Node()

    def insertIntoTrie(self, product):
        temp = self.root
        for p in product:
            if p not in temp.children:
                temp.children[p] = Node()
            temp = temp.children[p]
        temp.end = True

    def search(self, word):
        present = True
        temp = self.root
        current = ""
        for w in word:
            if w not in temp.children:
                present = False
                break
            current += w
            temp = temp.children[w]

        if not present:
            return []

        queue = deque([(current, temp)])

        result = []

        while len(queue):
            current, temp = queue.popleft()
            if temp.end:
                result.append(current)

            for key, value in temp.children.items():
                queue.append((current + key, value))

        return sorted(result)[:3]

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        for p in products:
            self.insertIntoTrie(p)
        
        result = []    
    
        for i in range(len(searchWord)):
            result.append(self.search(searchWord[0: i + 1]))
        
        return result