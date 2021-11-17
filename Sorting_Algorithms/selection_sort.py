def selection_sort(lst):
    '''
    selection sort

    ---------------->This is my solution based on the method below mentioned

    1) we need to select the minimum element in the list and swap the position of it 

    2) and the process goes on

    '''

    for x in range(len(lst) - 1):
        # position = 0
        # min = lst[x]

        position = x
        for y in range(x+1, len(lst)):

            if lst[y] < lst[position]:          #lst[y] < min:
                
                position = y
            
            
        # if position == 0:
        #     continue
        # else:
        lst[x], lst[position] = lst[position], lst[x]

    return lst


print(selection_sort([3,5,8,9,6,2]))
        

