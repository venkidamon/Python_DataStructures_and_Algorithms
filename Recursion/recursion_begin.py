def recursion(n):
    if n > 0:
        k = n**2
        print(k)
        recursion(n-1)

recursion(4)
