from binaryNode import BinaryNode
from BST import BinarySearchTree
from collections import deque


def serialize(root) -> str:
    if not root:
        return ""
    stack = [root]
    serialized = ""
    while stack:
        node = stack.pop()
        if not node:
            serialized += "*,"
        else:
            serialized += str(node.val) + ","
            stack.append(node.right)
            stack.append(node.left)
    with open("binaryTree.txt", "w") as bt:
        bt.write(serialized[:-1])


def deserialize(line: str):
    if not line:
        return None
    queue = deque(line.split(','))
    return helper(queue)

def helper(queue):
    value = queue.popleft()
    if value == "*":
        return None
    node = BinaryNode(int(value))
    node.left = helper(queue)
    node.right = helper(queue)
    return node
    



if __name__ == "__main__":
    node = BinaryNode(4)
    tree = BinarySearchTree(node)
    tree.add(BinaryNode(3))
    tree.add(BinaryNode(5))
    tree.add(BinaryNode(2))
    tree.add(BinaryNode(6))
    tree.add(BinaryNode(4))
    tree.add(BinaryNode(8))
    print(tree)
    serialize(tree.root)
    with open("binaryTree.txt", "r") as bt:
        line = bt.readline()
        root1 = deserialize(line)
        tree1 = BinarySearchTree(root1)
        print(tree1)

