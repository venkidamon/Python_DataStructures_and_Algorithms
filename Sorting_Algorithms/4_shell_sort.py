def shell_sort(lst):
    n = len(lst)
    gap = n//2
    while gap > 0:
        i = gap
        while i < n:
            temp = lst[i]
            j = i - gap
            while j >= 0 and lst[j] > temp:
                lst[j+gap] = lst[j]
                j = j-gap
            lst[j+gap] = temp
            i = i + 1
        gap = gap//2
    return lst

print(shell_sort([567,6573,43,4323,46,57,685,57856,4]))