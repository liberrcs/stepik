
n=int(input())
matrix=[]
flag=True 
for k in range(n):
    tmp=[int(x) for x in input().split()]
    matrix.append(tmp)
for i in range(n):
    for q in range(n):
        if matrix[i][q] != matrix[q][i] and i != q:
            flag=False
            break
if flag == True:
    print("YES")
else:
    print("NO")



