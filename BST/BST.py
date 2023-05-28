from binaryNode import BinaryNode
from collections import deque


class BinarySearchTree:
    def __init__(self, root = None) -> None:
        self.root = root

    def __repr__(self):
        if self.root is None:
            return "None"

        queue = deque([self.root])
        result = []

        while queue:
            node = queue.popleft()

            if node is not None:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")

        return ' '.join(result)

    # Recursively finds where the given node should be placed and
    # inserts it in a leaf at that point.
    def _insertInorder(self, subTreePtr, newNode):
        if subTreePtr is None:
            return newNode
        
        if newNode.val < subTreePtr.val:
            subTreePtr.left = self._insertInorder(subTreePtr.left, newNode)
        elif newNode.val > subTreePtr.val:
            subTreePtr.right = self._insertInorder(subTreePtr.right, newNode)
        
        return subTreePtr

    # Removes the given target value from the tree while maintaining a
    # binary search tree.
    def _removeByValue(self, root, key):
        if root is None:
            return None

        if key > root.val:
            root.right = self._removeByValue(root.right, key)
        elif key < root.val:
            root.left = self._removeByValue(root.left, key)
        else:
            # root is leaf
            if not root.left and not root.right:
                return None
            # root has only one child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # if there are two children
            else:
                # we can find max val from left subtree
                # or min val from right subtree
                min_node = self._findMin(root.right)
                root.val = min_node.val
                root.right = self.remove(root.right, min_node.val)
        return root

    def _findMin(self, node):
        tmp = node
        while tmp.left is not None:
            tmp = tmp.left
        return tmp

    # Removes a given node from a tree while maintaining a
    # binary search tree.
    def _removeNode(self, root, nodePtr):
        if root is None:
            return None

        if nodePtr.val > root.val:
            root.right = self._removeNode(root.right, nodePtr)
        elif nodePtr.val < root.val:
            root.left = self._removeNode(root.left, nodePtr)
        else:
            # root is leaf
            if not root.left and not root.right:
                return None
            # root has only one child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # if there are two children
            else:
                # we can find max val from left subtree
                # or min val from right subtree
                min_node = self._findMin(root.right)
                root.val = min_node.val
                root.right = self._removeNode(root.right, min_node)
        return root

    # Returns a pointer to the node containing the given value,
    # or None if not found.
    def _findNode(self, treePtr, target):
        if treePtr is None:
            return None
        
        if treePtr.val == target:
            return treePtr
        elif target > treePtr.val:
            return self._findNode(treePtr.right, target)
        else:
            return self._findNode(treePtr.left, target)

    def _getHeight(self, root) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self._getHeight(root.getLeftChild()), 
                           self._getHeight(root.getRightChild()))
        
    def _getNumberOfNodes(self, node):
        if node is None:
            return 0
        return 1 + self._getNumberOfNodes(node.left) + self._getNumberOfNodes(node.right)

    def isEmpty(self) -> bool:
        return self.root is None
        
    def getHeight(self):
        return self._getHeight(self.root)

    def getNumberOfNodes(self) -> int:
        return self._getNumberOfNodes(self.root)

    def getRootData(self):
        return self.root.val

    def setRootData(self, newData) -> None:
        self.root.val = newData

    def add(self, newEntry):
        self.root = self._insertInorder(self.root, newEntry)
        return self.root

    def remove(self, key) -> bool:
        self.root = self._removeByValue(self.root, key)
        return self.root
    
    def removeNode(self, node):
        self.root = self._removeNode(self.root, node)
        return self.root

    def clear(self) -> None:
        self.root = None

    def contains(self, anEntry) -> bool:
        if self._findNode(self.root, anEntry.val):
            return True
        return False

    def preorderTraverse(self, visit):
        visit(self.root)
        self._preorder(visit, self.root.left)
        self._preorder(visit, self.root.right)
    
    def inorderTraverse(self, visit, ):
        self._preorder(visit, self.root.left)
        visit(self.root)
        self._preorder(visit, self.root.right)

    def postorderTraverse(self, visit):
        self._preorder(visit, self.root.left)
        self._preorder(visit, self.root.right)
        visit(self.root)


