import random
#copied from https://www.geeksforgeeks.org/comparison-among-bubble-sort-selection-sort-and-insertion-sort/
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate a list of 10000 random integers
arr = [random.randint(1, 10000) for i in range(10000)]

# Sort the list using each algorithm and time it
import time

start_time = time.time()
bubble_sort(arr.copy())
bubble_sort_time = time.time() - start_time

start_time = time.time()
selection_sort(arr.copy())
selection_sort_time = time.time() - start_time

start_time = time.time()
insertion_sort(arr.copy())
insertion_sort_time = time.time() - start_time

print("Bubble Sort time:", bubble_sort_time)
print("Selection Sort time:", selection_sort_time)
print("Insertion Sort time:", insertion_sort_time)
