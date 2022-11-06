class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        res = sorted(list(zip(indices, sources, targets)), key = lambda k: k[0])
        
        indices, sources, targets = [], [], []
        
        for i, j, k in res:
            indices.append(i)
            sources.append(j)
            targets.append(k)
        
        s, new_s = s, []
        
        diff = indices[0] - 0
        
        if diff:
            new_s.append(s[0:diff])
        
        for i, ind in enumerate(indices):
                        
            length = len(sources[i])
            
            current = s[ind : ind + len(sources[i])]
            
            if current == sources[i]:
                new_s.append(targets[i])
                i1, j1 = indices[i] + length, len(s)
                
                if i < len(indices) - 1:
                    j1 = indices[i + 1]
            else:
                i1, j1 = ind, len(s)
                
                if i < len(indices) - 1:
                    j1 = ind + indices[i + 1] - indices[i]     
            
            if j1 - i1 > 0:
                new_s.append(s[i1:j1])
                        
        
        return "".join(new_s)