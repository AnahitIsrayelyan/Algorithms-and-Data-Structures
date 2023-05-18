class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return "->".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def length(self):
        tmp = self.head
        count = 0
        while tmp is not None:
            tmp = tmp.next
            count += 1
        return count

    def push_front(self, new_node: Node):
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_back(self, new_node: Node):
        if self.isEmpty():
            self.push_front(new_node)
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = new_node
            new_node.prev = tmp

    def insert_at_position(self, new_node: Node, position: int):
        tmp = self.head
        count = 0
        while tmp is not None:
            if count == position - 1:
                break
            count += 1
            tmp = tmp.next
        if position == 1:
            self.push_front(new_node)
        elif tmp is None:
            print("Can't insert at position ", position, ".")
        elif tmp.next is None:
            self.push_back(new_node)
        else:
            new_node.next = tmp.next
            new_node.prev = tmp
            tmp.next.prev = new_node
            tmp.next = new_node

    def insert_after(self, target_value, new_node: Node):
        if self.head is None:
            print("Is empty.")
            return
        
        for node in self:
            if node.data == target_value:
                if node.next is None:
                    node.next = new_node
                    new_node.prev = node
                else:
                    new_node.next = node.next
                    node.next.prev = new_node
                    new_node.prev = node
                    node.next = new_node
                return
            
        print("There is no such a value.")

    def remove(self, target_value):
        if self.head is None:
            print("Is empty")
            return
        
        if self.head.data == target_value:
            self.head = self.head.next
            return
        
        for node in self:
            if node.data == target_value:
                if node.next is None:
                    node.prev.next = None
                    node.prev = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node.next = None
                    node.prev = None
                return
        
        print("There is no such a value.")
           

    def find(self, target_value):
        if self.head is None:
            print("Is empty")
        count = 0
        for node in self:
            if node.data == target_value:
                return count
            count += 1
    


if __name__ == "__main__":
    x = DoublyLinkedList()
    print(x.isEmpty())
    x.push_front(Node(2))
    print(x)
    x.push_back(Node(5))
    print(x)
    x.insert_after(5, Node(4))
    print(x)
    x.insert_at_position(Node(1), 1)
    print(x)
    print(x.find(4))
    x.remove(4)
    print(x)
    print(x.length())