def binarysearch_rec(A, key, l, r):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binarysearch_rec(A, key, l, mid-1)
        elif key > A[mid]:
            return binarysearch_rec(A, key, mid+1, r)

A = [15, 21, 47, 84, 96]
found = binarysearch_rec(A,196,0,4)
print('Result:', found)
