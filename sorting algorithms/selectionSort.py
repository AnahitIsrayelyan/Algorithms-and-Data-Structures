from typing import List

def find_smallest(ls: List) -> int:
    smallest_index = 0
    smallest_element = ls[0]
    for i in range(1, len(ls)): 
        if ls[i] < smallest_element:
            smallest_element = ls[i]
            smallest_index = i
    return smallest_index


def selection_sort(ls: List) -> List:           # time complexity O(n^2)
    new_ls = []
    for _ in range(len(ls)):
        smallest_index = find_smallest(ls)
        new_ls.append(ls.pop(smallest_index))
    return new_ls


if __name__ == "__main__":
    ls = [3, -1, 5, 6, 90, 11, 909, -10]
    print(selection_sort(ls))