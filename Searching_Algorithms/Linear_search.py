def linear_search(arr, key):
    '''time complexity of linear search is O(n)'''
    index = 0
    while index < len(arr):
        if arr[index] == key:
            return index
        else:
            index += 1
    return -1


A = [84, 21, 47, 96, 15]

print(linear_search(A, 100))