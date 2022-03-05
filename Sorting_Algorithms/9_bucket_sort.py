def insertion_sort(lst):
    for index in range(1, len(lst)):
        current_value = lst[index]
        position = index
        while position > 0 and lst[position-1]>current_value:
            lst[position] = lst[position - 1]
            position = position - 1
        lst[position] = current_value

def bucket_sort(arr):
    n = len(arr)
    arr_max = max(arr)
    l = []
    buckets = [l] * 10
    for x in range(n):
        j = int((n*arr[x])/(arr_max + 1))
        if len(buckets[j]) == 0:
            buckets[j] = [arr[x]]
        else:
            buckets[j].append(arr[x])

    for x in range(10):
        insertion_sort(buckets[x])

    k = 0
    for x in range(10):
        for j in range(len(buckets[x])):
            arr[k] = buckets[x].pop(0)
            k = k+1

    print(arr)


bucket_sort([4343,34,23,24,34,2342,4234,24])
