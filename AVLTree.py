class AVLNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self) -> None:
        self.root = None


    def insert(self, root, val):
        if not root:
            return AVLNode(val)
        
        if val <= root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and val < root.left.val:
            return self.rightRotate(root)
        
        if balance > 1 and val > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and val > root.right.val:
            return self.leftRotate(root)
        
        if balance < -1 and val < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    

    def delete(self, root, val):
        if root is None:
            return None

        if val > root.val:
            root.right = self.delete(root.right, val)
        elif val < root.val:
            root.left = self.delete(root.left, val)
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
                root.right = self.delete(root.right, min_node.val)

        if not root:
            return root
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and val < root.left.val:
            return self.rightRotate(root)
        
        if balance > 1 and val > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and val > root.right.val:
            return self.leftRotate(root)
        
        if balance < -1 and val < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    

    def search(self, root, val):
        if not root:
            return False
        
        if val == root.val:
            return True
        elif val > root.val:
            return self.search(root.right, val)
        else:
            return self.search(root.left, val)


    def _findMin(self, node):
        tmp = node
        while tmp.left is not None:
            tmp = tmp.left
        return tmp
    

    def _findMax(self, node):
        tmp = node
        while tmp.right is not None:
            tmp = tmp.right
        return tmp


    def rightRotate(self, root):
        new_root = root.left
        tmp = new_root.right

        root.left = tmp
        new_root.right = root

        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))
        new_root.height = 1 + max(self.getHeight(new_root.right), self.getHeight(new_root.left))

        return new_root


    def leftRotate(self, root):
        new_root = root.right
        tmp = new_root.left

        root.right = tmp
        new_root.left = root

        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))
        new_root.height = 1 + max(self.getHeight(new_root.right), self.getHeight(new_root.left))

        return new_root


    def getBalance(self, root):
        if not root:
            return 0
        return (self.getHeight(root.left) - self.getHeight(root.right))
    

    def getHeight(self, root):
        if not root:
            return 0
        
        return root.height
    

    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    
    def inOrder(self, root):
 
        if not root:
            return
 
        self.preOrder(root.left)
        print("{0} ".format(root.val), end="")
        self.preOrder(root.right)

    
    def postOrder(self, root):
 
        if not root:
            return
 
        self.preOrder(root.left)
        self.preOrder(root.right)
        print("{0} ".format(root.val), end="")


if __name__ == "__main__":
    myTree = AVLTree()
    root = None
    
    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 5)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)
    myTree.preOrder(root)
    print()
    root = myTree.delete(root, 20)
    myTree.preOrder(root)
    print()
    print(myTree.search(root, 90))
    print(myTree._findMin(root).val)
 
    