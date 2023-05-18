from random import randint
import time
from singlyLinkedList import *
from typing import List


def find(ls: List, val: int):
    for i in range(len(ls)):
        if ls[i] == val:
            return i


linkedList1 = LinkedList()
linkedList2 = LinkedList()
linkedList3 = LinkedList()
list1 = [0] * 1000
list2 = [0] * 10000
list3 = [0] * 100000

for i in range(1000):
    # tmp = randint(0, 1000)
    list1[i] = i
    rand_node = Node(i)
    linkedList1.push_front(rand_node)

for i in range(10000):
    # tmp = randint(0, 10000)
    list2[i] = i
    rand_node = Node(i)
    linkedList2.push_front(rand_node)

for i in range(100000):
    # tmp = randint(0, 100000)
    list3[i] = i
    rand_node = Node(i)
    linkedList3.push_front(rand_node)


rand_int1 =  500 # randint(0,1000)
rand_int2 =  5000 # randint(0, 10000)
rand_int3 = 50000 # randint(0, 100000)


tmp_node = Node(1)


### for 1000 elem

precision = 20
# insert
lstart = time.time()
linkedList1.insert_after(rand_int1, tmp_node)
lend = time.time()

target_index = find(list1, rand_int1) + 1
start = time.time()
list1.insert(target_index, 1)
end = time.time()

print("Insert for linked list (1000): ", round((lend - lstart), precision))
print("Insert for list (1000): ", round((end - start), precision))

# find
lstart = time.time()
linkedList1.find(rand_int1)
lend = time.time()

start = time.time()
find(list1, rand_int1)
end = time.time()

print("Find for linked list (1000): ", round((lend - lstart), precision))
print("Find for list (1000): ", round((end - start), precision))

# remove
lstart = time.time()
linkedList1.remove(rand_int1)
lend = time.time()

start = time.time()
list1.remove(rand_int1)
end = time.time()

print("Remove for linked list (1000): ", round((lend - lstart), precision))
print("Remove for list (1000): ", round((end - start), precision))

print()
### for 10000 elem

precision = 20
# insert
lstart = time.time()
linkedList2.insert_after(rand_int2, tmp_node)
lend = time.time()

target_index = find(list2, rand_int2) + 1
start = time.time()
list2.insert(target_index, 1)
end = time.time()

print("Insert for linked list (10000): ", round((lend - lstart), precision))
print("Insert for list (10000): ", round((end - start), precision))

# find
lstart = time.time()
linkedList2.find(rand_int2)
lend = time.time()

start = time.time()
find(list2, rand_int2)
end = time.time()

print("Find for linked list (10000): ", round((lend - lstart), precision))
print("Find for list (10000): ", round((end - start), precision))

# remove
lstart = time.time()
linkedList2.remove(rand_int2)
lend = time.time()

start = time.time()
list2.remove(rand_int2)
end = time.time()

print("Remove for linked list (10000): ", round((lend - lstart), precision))
print("Remove for list (10000): ", round((end - start), precision))


print()
### for 100000 elem

precision = 20
# insert
lstart = time.time()
linkedList2.insert_after(rand_int3, tmp_node)
lend = time.time()

target_index = find(list3, rand_int3) + 1
start = time.time()
list2.insert(target_index, 1)
end = time.time()

print("Insert for linked list (100000): ", round((lend - lstart), precision))
print("Insert for list (100000): ", round((end - start), precision))

# find
lstart = time.time()
linkedList3.find(rand_int3)
lend = time.time()

start = time.time()
find(list3, rand_int3)
end = time.time()

print("Find for linked list (100000): ", round((lend - lstart), precision))
print("Find for list (100000): ", round((end - start), precision))

# remove
lstart = time.time()
linkedList3.remove(rand_int3)
lend = time.time()

start = time.time()
list3.remove(rand_int3)
end = time.time()

print("Remove for linked list (100000): ", round((lend - lstart), precision))
print("Remove for list (100000): ", round((end - start), precision))
