from typing import List

def insertion_sort(ls: List):
    if len(ls) <= 1:
        return
    for i in range(1, len(ls)):
        key = ls[i]    
        j = i - 1      
        while j >= 0 and key < ls[j]:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = key

# worst case O(n^2)
# best case O(n)


if __name__ == "__main__":
    ls = [2,1,0,6,5,4]
    insertion_sort(ls)
    print(ls)