def bubble_sort(lst):
    for x in range(len(lst)-1):
        for y in range(0, len(lst)-x-1):
            if lst[y] > lst[y + 1]:
                lst[y],lst[y+1] = lst[y+1],lst[y]
    return lst

print(bubble_sort([3,5,8,9,6,2,32,4324,243,324,2,3,5,64,587,64,64,2,2,3]))
