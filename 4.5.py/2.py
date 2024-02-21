
n,m=int(input()), int(input())
matrix=[]
for i in range(n):
    tmp=[int(x) for x in input().split()]
    matrix.append(tmp)
x=0
y=0
matrix_max=matrix[0][0]
for k in range(n):
    for q in range(m):
        if matrix[k][q] > matrix_max:
            matrix_max=matrix[k][q]
            x=k
            y=q
print(x,y)


