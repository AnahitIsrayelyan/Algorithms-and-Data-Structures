from typing import List 

def partition(ls: List, l: int, r: int):
    pivot = ls[r]
    i = l - 1
    for j in range(l, r):
        if ls[j] < pivot:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]
    ls[i + 1], ls[r] = ls[r], ls[i + 1]
    return (i+1)

def quick_sort(ls: List, l: int, r: int):
    if l < r:
        pivot = partition(ls, l, r)
        quick_sort(ls, l, pivot - 1)
        quick_sort(ls, pivot + 1, r)


# advantage: sorting in place, unlike merge sort
# best-case, also average case scenario O(n log n)
# worst case scenario O(n^2)
# D&C

if __name__ == "__main__":
    ls = [3, -1, 5, 6, 6, 90, 11, 909, -10]
    quick_sort(ls, 0, len(ls) - 1)
    print(ls)