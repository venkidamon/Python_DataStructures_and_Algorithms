def binary_search(arr, key):
    '''binary sort has more efficiency than linear or sequential sort.
        Only works when array is SORTED'''
    
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return "Successful"
        elif key < arr[mid]:
            right = mid - 1
        elif key > arr[mid]:
            left = mid + 1
        else:
            return "Not found"

    return "Not found"


A = [1,2,3,4,5,6,7,8,9]

print(binary_search(A, 10))
    