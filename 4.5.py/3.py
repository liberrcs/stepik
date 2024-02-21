
n,m=int(input()), int(input())
matrix=[]
for k in range(n):
    tmp=[int(x) for x in input().split()]
    matrix.append(tmp)
x,y = [int(i) for i in input().split()]
for i in range(n):
    matrix[i][x], matrix[i][y] = matrix[i][y],matrix[i][x]
for q in range(n):
    print(*matrix[q])

    



