def shell_sort(lst):
    gap = len(lst)//2
    for x in range(len(lst)-gap):
        for y in range(x, len(lst) - gap):
            if lst[y] > lst[y + gap]:
                lst[y], lst[y + gap] = lst[y + gap],lst[y]
            if y-gap >= 0:
                if lst[y] < lst[y-gap]:
                    lst[y], lst[y-gap] = lst[y-gap],lst[y]
        gap = gap//2
    return lst

print(shell_sort([567,6573,43,4323,46,57,685,57856,4])) #in this program there are some error that are need to be corrected
