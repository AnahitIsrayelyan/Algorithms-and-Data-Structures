from BST import BinarySearchTree
from binaryNode import BinaryNode

if __name__ == "__main__":
    node = BinaryNode(1)
    tree = BinarySearchTree(node)
    print()
    print("Here is the value of root, must be 1: ", tree.getRootData())
    node = BinaryNode(2)
    print()
    tree.add(node)
    print("Checking add, must be 1 None 2:",tree)
    print()
    print("Checking getHeight, must be 2:", tree.getHeight())
    print()
    node1 = BinaryNode(4)
    print("Checking contains, must be True:", tree.contains(node))
    print("Checking contains, must be False:", tree.contains(node1))
    print()
    print("Checking getNumberOfNodes, must be 2:", tree.getNumberOfNodes())
    print()
    tree.remove(2)
    print("Checking remove, must be 1:", tree)
    print()
    tree.removeNode(tree.root)
    print("Checking removeNode, must be None:", tree)
    print()
    print("Checking isEmpty, must be True: ", tree.isEmpty())
    print()
    tree.add(BinaryNode(3))
    tree.add(BinaryNode(4))
    print(f"Before clear isEmpty: {tree.isEmpty()}")
    tree.clear()
    print(f"After clear isEmpty: {tree.isEmpty()}")

    

