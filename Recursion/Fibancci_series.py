def fibanacci_series(n):
    '''To print all the fibanacci series up to n using recursion'''
    if n == 0 or n == 1:
        return n
    else:
        return fibanacci_series(n-1) + fibanacci_series(n-2)


        
for x in range(0,5):

    print(fibanacci_series(x))