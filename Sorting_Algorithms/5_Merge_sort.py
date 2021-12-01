def merge_sort(lst, left, right):
    if left < right:
        mid = (left + right)//2
        merge_sort(lst, left, mid)
        merge_sort(lst, mid+1, right)
        merge(lst, left, mid, right)

def merge(lst, left, mid, right):
    i = left
    j = mid+1
    k = left
    temp_lst = [0] * (right + 1)
    while i <= mid and j <= right:
        if lst[i] < lst[j]:
            temp_lst[k] = lst[i]
            i += 1
        else:
            temp_lst[k] = lst[j]
            j += 1
        k += 1

    while i <= mid:
        temp_lst[k] = lst[i]
        i += 1
        k += 1

    while j <= right:
        temp_lst[k] = lst[j]
        j += 1
        k += 1
    for x in range(left, right+1):
        lst[x] = temp_lst[x]


A = [3,5,8,9,6,2]

merge_sort(A, 0, len(A)-1)

