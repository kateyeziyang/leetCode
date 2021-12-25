from typing import DefaultDict, List
from collections import defaultdict, deque

class Node:
    def __init__(self) -> None:
        self.children = defaultdict(Node)
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = Node()
    
    def find(self,path):
        cur = self.root
        if len(path)==1:
            return self.root
        for word in path.split("/")[1:]:
            cur = cur.children[word]
        return cur

    def ls(self, path: str) -> List[str]:
        cur = self.find(path)
        if cur.content:
            return [path.split("/")[-1]]
        return sorted(cur.children.keys())

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur=self.find(filePath)
        cur.content+=content

    def readContentFromFile(self, filePath: str) -> str:
        return self.find(filePath).content

# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)