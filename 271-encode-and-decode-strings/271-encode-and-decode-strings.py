class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        
        for current in strs:
            result += str(len(current)) + "_" + current
        
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
                
        while i < len(s):
            length = ''
            while s[i].isdigit():
                length += s[i]
                i += 1
            i = i + 1
            
            length = int(length)
            result.append(s[i: i + length])
            i = i + length
            
        return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))