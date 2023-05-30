from singlyLinkedList import *


class HashTable:
    def __init__(self) -> None:
        self.capacity = 99
        self.array = [None] * self.capacity

    def hashFunction(self, key: str) -> int:
        summ = 0
        for char in key:
            summ += ord(char)
        return (summ // self.capacity)
    
    def set(self, key: str, value: int):
        hashValue = self.hashFunction(key)
        if self.array[hashValue] is None:
            self.array[hashValue] = LinkedList()
        self.array[hashValue].push_front(Node(key, value))

    def get(self, key: str) -> int:
        hashValue = self.hashFunction(key)
        return self.array[hashValue].find(key) if self.array[hashValue] else None
    
    def remove(self, key):
        hashValue = self.hashFunction(key)
        self.array[hashValue].remove(key)


if __name__ == "__main__":
    tab = HashTable()
    tab.set('Anahit', 20)
    tab.set('Lyusi', 30)
    tab.set('Samvel', 40)

    print(tab.get('Lyusi'))
    print(tab.get('Anna'))
    print(tab.get('Anahit'))

    print(tab.array[tab.hashFunction('Lyusi')])
    tab.remove('Lyusi')
    print(tab.array[tab.hashFunction('Lyusi')])



