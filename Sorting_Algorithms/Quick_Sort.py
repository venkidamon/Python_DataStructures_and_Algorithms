def quicksort(array):
    _quicksort(array, 0, len(array) - 1)
    return array
 
def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1 
        print(array)
        _quicksort(array, start, right)
        _quicksort(array, left, stop)





test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))