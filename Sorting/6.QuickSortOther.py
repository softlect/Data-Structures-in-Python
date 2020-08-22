def partition(A, low, high):
    i = low - 1
    pivot = A[high]
    for j in range(low, high):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1


def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi - 1)
        quicksort(A, pi + 1, high)


#A = [3, 5, 8, 9, 6, 2]
A = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
n = len(A)
print('Original Array:',A)
quicksort(A, 0, n - 1)
print('Sorted Array:',A)


