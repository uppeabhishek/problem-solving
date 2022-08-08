class Solution:
                
    def getNextWords(self, wordList):
        dic = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                dic[word[:i] + '*' + word[i + 1:]].append(word)
        return dic
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
                
        dictionary = self.getNextWords(wordList)

        visited = set([beginWord])
        queue = deque([(beginWord, 1)])
        
        while len(queue):
                    
            word, distance = queue.popleft()
            
            if word == endWord:
                return distance
            
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                for w in dictionary[key]:
                    if w not in visited:
                        queue.append((w, distance + 1))
                    visited.add(w)           
        return 0
            
        
        
        