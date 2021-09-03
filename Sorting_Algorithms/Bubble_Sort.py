def bubble_sort(arr):
    length = len(arr)
    for ele in range(length - 1):
        for val in range(length - ele - 1):
            if arr[val] > arr[val + 1]:
                arr[val], arr[val + 1] = arr[val + 1],arr[val]
    return arr

print(bubble_sort([5,9,3,2,7,1,0]))
