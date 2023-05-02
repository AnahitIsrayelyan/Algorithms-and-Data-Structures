from time import time

def bubble_sort(ls):
    for _ in range(len(ls)):
        for j in range(len(ls) - 1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]

def optimized_bubble_sort(ls):
    swapped = True
    iterations = 0
    while(swapped):
        swapped = False
        for i in range(len(ls) - iterations - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True
        iterations += 1


if __name__ == "__main__":
    ls1 = [2, 1, 3, 4, 5]
    ls = [2, 1, 3, 4, 5]
    bubble_sort(ls1)
    print(ls1)
    optimized_bubble_sort(ls)
    print(ls)
