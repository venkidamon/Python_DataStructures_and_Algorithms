def natural_numbers_sum(n):
    '''sum of n natural numbers using recursion'''
    if n == 1:
        return 1
    else:
        return natural_numbers_sum(n-1) + n



print(natural_numbers_sum(5))