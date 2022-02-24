class Solution:
        
    def simplifyPath(self, path: str) -> str:
        stack = deque(["/"])
        i = 1
        while i < len(path):
            temp = []
            while i < len(path)  and path[i] != "/":
                temp.append(path[i])
                i += 1
            if len(temp) > 0:
                if len(temp) == 2 and temp[0] == "." and temp[1] == ".":
                    if len(stack) > 0:
                        stack.pop()
                elif not (len(temp) == 1 and temp[0] == "."):
                    stack.append("".join(temp))
            else:
                i += 1

        if len(stack) and stack[0] == "/":
            stack.popleft()

        if len(stack) == 0:
            return "/"

        result = ""
        while len(stack):
            result += "/" + stack.popleft()

        return result
                    