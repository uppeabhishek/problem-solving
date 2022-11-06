from collections import defaultdict
from typing import List


class Node:
    def __init__(self):
        self.path = defaultdict(Node)
        self.files = defaultdict(str)


class FileSystem:

    def __init__(self):
        self.root = Node()
        self.root.path['/'] = Node()

    def getPathArray(self, path):
        if path == "/":
            return ["/"]

        path = path.split("/")
        path[0] = '/'
        return path

    def ls(self, path: str) -> List[str]:
        path = self.getPathArray(path)

        last = path[-1]

        temp = self.root

        result = []

        for p in path[0:len(path) - 1]:
            if p in temp.path:
                temp = temp.path[p]

        if last in temp.files:
            result.append(last)
        else:
            temp = temp.path[last]
            result = list(temp.files.keys()) + list(temp.path.keys())
            result.sort()

        return result

    def mkdir(self, path: str) -> None:
        path = self.getPathArray(path)

        temp = self.root

        for p in path:
            if p not in temp.path:
                temp.path[p] = Node()
            temp = temp.path[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = self.getPathArray(filePath)
        fileName = path[-1]

        temp = self.root
        for p in path[0:len(path) - 1]:
            temp = temp.path[p]

        if fileName in temp.files:
            temp.files[fileName] += content
        else:
            temp.files[fileName] = content

    def readContentFromFile(self, filePath: str) -> str:
        path = self.getPathArray(filePath)
        fileName = path[-1]

        temp = self.root
        for p in path[0:len(path) - 1]:
            temp = temp.path[p]

        return temp.files[fileName]


obj = FileSystem()
obj.mkdir("/goowmfn")
print(obj.ls("/goowmfn"))
print(obj.ls("/"))
obj.mkdir("/z")
print(obj.ls("/"))
print(obj.ls("/"))
obj.addContentToFile("/goowmfn/c", "shetopcy")
print(obj.ls("/z"))
print(obj.ls("/goowmfn/c"))
print(obj.ls("/goowmfn"))
