def radix_sort(A):
    n = len(A)
    max_element = max(A)
    digits = len(str(max_element))
    l = []
    bins = [l] * 10
    for i in range(digits):
        for j in range(n):
            e = int((A[j]/pow(10, i))%10)
            if len(bins[e])> 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k = k+1
A = [23,5,5,5,645,465,46,546,54,65,53,45,435,43]
radix_sort(A)
print(A)