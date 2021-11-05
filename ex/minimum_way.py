def make_step(k):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                if i > 0 and m[i-1][j] == 0 and arr[i-1][j] == 1:
                    m[i-1][j] = k+1
                if j > 0 and [i][j-1] == 0 and arr[i][j-1] == 1:
                    m[i][j-1] = k+1
                if i < len(m)-1 and m[i+1][j] == 0 and arr[i+1][j] == 1:
                    m[i+1][j] = k +1
                if j < len(m[i])-1 and m[i][j+1] == 0 and arr[i][j+1] == 1:
                    m[i][j+1] = k+1

    print(m)




def minimum_path(area):
    i,j = 0, 0
    r, c = 0, 0

    for x in range(0, len(area)):
        c = 0
        for y in range(0, len(area[x])):
            if area[x][y] == 9:
                break
            c += 1
        r += 1
    

    start = i, j
    end =[]
    end.append(r-1)
    end.append(c)
    return end

                                                          



arr = [[1,0,0],[1,0,0],[1,9,1]]
result = minimum_path(arr)
print(result)

m = []
for f in range(len(arr)):
    m.append([])
    for g in range(len(arr[f])):
        m[-1].append(0)
m[0][0] = 1
print(m)  

k = 0
print(m[result[0]][result[1]])
while m[result[0]][result[1]] == 0:
    k+=1
    make_step(k)

