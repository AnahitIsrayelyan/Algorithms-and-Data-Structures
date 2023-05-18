from doublyLinkedList import Node, DoublyLinkedList

class ExtendedNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.snext = None   # snext for sorted next
        self.nprev = None   # sprev for sorted prev

class SortedDoublyLinkedList(DoublyLinkedList):
    
    def __init__(self) -> None:
        super().__init__()
        self.shead = None     # shead for sorted head
    
    
    def __iter__(self):
        return super().__iter__()


    def __repr__(self):
        return super().__repr__()
    

    def __insert_sorted(self, new_node: ExtendedNode):
        if self.shead is None:
            self.shead = new_node
        elif self.shead.data >= new_node.data:
            new_node.snext = self.shead
            self.shead.sprev = new_node
            self.shead = new_node
        else:
            node = self.shead
            while node.snext is not None:
                if node.data >= new_node.data:
                    node.sprev.snext = new_node
                    new_node.sprev = node.sprev
                    node.sprev = new_node
                    new_node.snext = node
                    break
                node = node.snext
            if node.data >= new_node.data:
                node.sprev.snext = new_node
                new_node.sprev = node.sprev
                node.sprev = new_node
                new_node.snext = node
            else:
                node.snext = new_node
                new_node.sprev = node               #  rewrite

        
    def __remove_sorted(self, target_value):
        if self.shead is None:
            return

        if self.shead.data == target_value:
            self.shead = self.shead.snext
            if self.shead:
                self.shead.sprev = None
            return
        
        node = self.shead
        while node is not None:
            if node.data == target_value:
                if node.sprev:
                    node.sprev.snext = node.snext
                if node.snext:
                    node.snext.sprev = node.sprev
                node.snext = None
                node.sprev = None
                return
            node = node.snext
    

    def print_sorted(self):
        node = self.shead
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.snext
        nodes.append("None")
        print("->".join(nodes))


    def push_front(self, new_node: ExtendedNode):
        super().push_front(new_node)
        self.__insert_sorted(new_node)


    def push_back(self, new_node: ExtendedNode):
        super().push_back(new_node)
        self.__insert_sorted(new_node)


    def insert_at_position(self, new_node: ExtendedNode, position: int):
        tmp = self.head
        count = 0
        while tmp is not None:
            if count == position - 1:
                break
            count += 1
            tmp = tmp.next
        if position == 1:
            super().push_front(new_node)
        elif tmp is None:
            print("Can't insert at position ", position, ".")
        elif tmp.next is None:
            super().push_back(new_node)
        else:
            new_node.next = tmp.next
            new_node.prev = tmp
            tmp.next.prev = new_node
            tmp.next = new_node
        self.__insert_sorted(new_node)


    def insert_after(self, target_value, new_node: ExtendedNode):
        super().insert_after(target_value,new_node)
        self.__insert_sorted(new_node)
            

    def remove(self, target_value):
        super().remove(target_value)
        self.__remove_sorted(target_value)
        


if __name__ == "__main__":
    x = SortedDoublyLinkedList()
    print(x.isEmpty())
    x.push_front(ExtendedNode(2))
    print("ordinary:",x)
    x.print_sorted()
    x.push_back(ExtendedNode(5))
    print("ordinary:",x)
    x.print_sorted()
    x.push_front(ExtendedNode(10))
    print("ordinary:",x)
    x.print_sorted()
    x.insert_after(5, ExtendedNode(4))
    print("ordinary:",x)
    x.print_sorted()
    x.insert_at_position(ExtendedNode(1), 1)
    print("ordinary:",x)
    x.print_sorted()
    print(x.find(5))
    x.remove(2)
    print("ordinary:",x)
    x.print_sorted()
    print(x.length())
