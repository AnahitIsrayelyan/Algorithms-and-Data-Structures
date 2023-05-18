from singlyLinkedList import *


if __name__ == "__main__":
    linked_list = LinkedList()
    print("Before push_front:", linked_list)
    linked_list.push_front(Node(3))
    linked_list.push_front(Node(5))
    linked_list.push_front(Node(1))
    print("After push_front:", linked_list)
    linked_list.remove(3)
    print("After remove:", linked_list)
    linked_list.insert_after(5, Node(10))
    print("After insert:", linked_list)
    linked_list.find(5)
    linked_list.find(6)
