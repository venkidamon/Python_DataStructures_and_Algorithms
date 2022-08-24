from operator import le
from turtle import right
from winreg import LoadKey


def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    mid = (0 + len(arr)) // 2
    if(left <= right):
        if arr[mid] == key:
            return "Successful"
        elif key < arr[mid]:
            return binary_search(arr[0:mid], key)
        elif key > arr[mid]:
            return binary_search(arr[mid+1: len(arr)], key)
    else:
        return "Not found"

arr = [1,2,3,4,5]
print(binary_search(arr, -1))