class BinaryNode:
    def __init__(self, val = None, left = None, right = None) -> None:
        self.val = val
        self.left = left  
        self.right = right

    def setItem(self, item):
        self.val = item

    def getItem(self):
        return self.val

    def isLeaf(self):
        return (self.left is None and self.right is None)

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setLeftChild(self, left):   # left is type of BinaryNode
        self.left = left

    def setRightChild(self, right):   # right is type of BinaryNode
        self.right = right