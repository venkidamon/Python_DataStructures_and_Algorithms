def insertion_sort(lst):
    for x in range(len(lst) - 1):
        element = lst[x]
        if element > lst[x+1]:
            element = lst[x+1]
            for y in range(x, -1, -1):
                if lst[y] > element:
                    lst[y], lst[y+1] = lst[y+1], lst[y]
                else:
                    break

    return lst


lst = [423,42,3,2342,3]

print(insertion_sort(lst))
