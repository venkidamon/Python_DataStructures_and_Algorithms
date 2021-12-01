def quick_sort(A, low, high):
    if low < high:
        pivot_index = partition(A, low, high)
        quick_sort(A, low, pivot_index-1)
        quick_sort(A, pivot_index+1, high)

def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j  and A[i] <= pivot:
            i = i+1
        while i <= j and A[j] > pivot:
            j = j-1
        if i < j:
            A[i], A[j] = A[j],A[i]
        else:
            break
    print(A)
    A[low], A[j] = A[j], A[low]
    return j


A = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quick_sort(A, 0, len(A)-1)
print(A)




 