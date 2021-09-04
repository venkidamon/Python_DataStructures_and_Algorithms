def merge_sort(arr, cond, descending=False):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left, cond)
        merge_sort(right, cond)
        i = j = k = 0
        while i < len(left) and j < len(right):
            
            if left[i][cond] <= right[j][cond]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
            

        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        if descending == True:
            new_list = []
            len1= len(arr)
            for x in range(len1):
                new_list.append(arr.pop())
            return new_list
        else:
            return arr



elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
print(elements)
print('----------------------------------')
print(merge_sort(elements, 'age', descending=True))

