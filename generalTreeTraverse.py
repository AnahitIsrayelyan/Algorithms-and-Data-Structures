from typing import List
from collections import deque


class GTree_node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.children: List['GTree_node'] = [] 

    def remove_value(self):
        self.Value = None

    def insert_value(self, value):
        self.value = value

    
class GTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value, *indices):
        if self.root is None:
            self.root = GTree_node()

        current_node = self.root
        for index in indices:
            children_count = len(current_node.children)

            if index < 0 or index > children_count:
                raise IndexError("Invalid index specified")

            if index == children_count:
                new_node = GTree_node()
                current_node.children.append(new_node)
                current_node = new_node
            else:
                current_node = current_node.children[index]

        current_node.value = value

    def execute(self, input_value: int):
        if self.root is None:
            return None
        
        queue = deque()
        queue.append(self.root)

        while queue:
            current_node = queue.popleft()

            if current_node.value is not None:
                input_value = current_node.value(input_value)

            for child in current_node.children:
                queue.append(child)

        return input_value




def f1(x: int):
    return x*x

def f2(x: int):
    return x / 10

def f3(x: int):
    return 1 - x

def f4(x: int):
    return x/3

def f5(x: int):
    return x*2

def f6(x: int):
    return x+1



if __name__ == "__main__":
    tree = GTree()
    tree.root = GTree_node(f1)
    tree.root.children.append(GTree_node(f2))
    tree.root.children.append(GTree_node(f3))
    tree.root.children[0].children.append(GTree_node(f4))
    tree.root.children[1].children.append(GTree_node(f5))
    tree.root.children[1].children.append(GTree_node(f6))
    
    tree.insert(f1, 0, 1)

    print(tree.execute(4))