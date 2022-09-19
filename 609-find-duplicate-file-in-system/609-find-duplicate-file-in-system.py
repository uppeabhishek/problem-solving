class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        dictionary = defaultdict(list)
        
        
        for path in paths:
            
            directory, *files = path.split(" ")
            
            for file in files:
                current_file, content = file.split("(")
                content = content.split(")")[0]
                
                dictionary[content].append(directory + "/" + current_file)
                
        result = []
        
        for value in dictionary.values():
            if len(value) > 1:
                result.append(value)
        
        return result
            
                
            
            