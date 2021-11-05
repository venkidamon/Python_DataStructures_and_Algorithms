class Binary_Heap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    

    def precUp(self, i):
        while i//2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                tmp = self.heap_list[i//2]
                self.heap_list[i//2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.precUp(self.current_size)

    def precDowm(self, i):
        while(i*2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc
    
    def min_child(self, i):
        if i * 2 + 1 >self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

        
    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.precDowm(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while (i > 0):
            self.precDowm(i)
            i = i - 1

x = Binary_Heap()

x.buildHeap([9, 6, 5, 2, 3])
x.insert(1)
print(x.heap_list)