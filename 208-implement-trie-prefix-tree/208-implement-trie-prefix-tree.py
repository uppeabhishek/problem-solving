class Node:
    def __init__(self, end = False):
        self.children = defaultdict(Node)
        self.end = end
        
        
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.children:
                temp.children[c] = Node()  
            temp = temp.children[c]
        temp.end = True
        
    def search(self, word: str) -> bool:
        temp = self.root
        for c in word:
            if c not in temp.children:
                return False 
            temp = temp.children[c]
        return temp.end == True

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)