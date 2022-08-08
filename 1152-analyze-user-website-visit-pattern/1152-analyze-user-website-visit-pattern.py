class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        
        username = [x for _, x in sorted(zip(timestamp, username), key=lambda pair: pair[0])]
        website = [x for _, x in sorted(zip(timestamp, website), key=lambda pair: pair[0])]
        timestamp.sort()
                
        dic = defaultdict(list)
        for i in range(len(username)):
            dic[username[i]].append(website[i])
        
                
        result = defaultdict(set)
                
        max_val = 0
        
        for key, value in dic.items():
            if len(value) > 2:
                for j in range(len(value) - 2):
                    for k in range(j + 1, len(value) - 1):
                        for l in range(k + 1, len(value)):
                            temp = (value[j], value[k], value[l])                            
                            result[temp].add(key)
        
        max_val = 0
        
        for key, value in result.items():
            max_val = max(max_val, len(value))
            
        final = []
        
        for key, value in result.items():
            if len(value) == max_val:
                final.append(key)
        
        final.sort()
        
        return final[0]
            