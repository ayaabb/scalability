import random
from results_operations.calculate_runtime import *


def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1


def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def calculate_search_results():
    arrays = []
    sizes = [10 ** size for size in range(1, 8)] + [10 ** size // 2 for size in range(5, 8)]
    sizes = sorted(sizes)
    for size in sizes:
        arrays.append([i for i in range(size)])
    fast_results = []
    slow_results = []
    for arr in arrays:
        target = random.choice(arr)
        slow_result = calculate_runtime(linear_search, arr, target)
        fast_result = calculate_runtime(binary_search, arr, target)
        fast_results.append(fast_result)
        slow_results.append(slow_result)
    sizes = [len(arr) for arr in arrays]
    return sizes, slow_results, fast_results


