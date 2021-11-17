def bin_recursion(arr, key):
    left = 0
    right = len(arr) 
    while left <= right:
        mid = (left + right)//2
        if len(arr) == 0:
            return "Not Found"
        else:
            if arr[mid] == key:
                return "Successful"
            elif key < arr[mid]:
                return bin_recursion(arr[left : mid], key)
            elif key > arr[mid]:
                return bin_recursion(arr[mid+1 : right], key)
            else:
                return "Not Found"


A = [1,2,3,4]
print(bin_recursion(A, 5))