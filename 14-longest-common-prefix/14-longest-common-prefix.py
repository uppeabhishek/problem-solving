class Node:
    def __init__(self, end = False):
        self.children = defaultdict(Node)
        self.end = end
class Solution:
    
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.children:
                temp.children[c] = Node()  
            temp = temp.children[c]
        temp.end = True
        
    def search(self):
        temp = self.root
        result = []

        while temp.end != True:
            if len(temp.children) == 0 or len(temp.children) > 1:
                break
                
            key = list(temp.children.keys())[0]     
            result.append(key)
            temp = temp.children[key]
            
            
        return "".join(result)
            
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for str1 in strs:
            self.insert(str1)
        
        return self.search()
       