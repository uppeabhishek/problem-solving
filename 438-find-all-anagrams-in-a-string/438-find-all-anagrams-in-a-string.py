class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_counter = Counter()

        actual_counter = Counter(p)

        p_length = len(p)
        
        def isCounterMatched():
            if len(p_counter) != len(actual_counter):
                return False

            for key, value in p_counter.items():
                if key not in actual_counter or actual_counter[key] != value:
                    return False

            return True

            
        def helper():

            nonlocal p_counter, actual_counter

            result = []

            i = 0

            while i < len(s):
                current = s[i]
                
                if i >= p_length:
                    p_counter[s[i - p_length]] -= 1
                    if not p_counter[s[i - p_length]]:
                        del p_counter[s[i - p_length]]
                    
                p_counter[current] += 1
                
                if isCounterMatched():
                    result.append(i + 1 - p_length)
                
                i += 1
        
            return result
                
        return helper()