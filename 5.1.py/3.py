
n=int(input())
matrix=[]
for k in range(n):
    tmp=[int(x) for x in input().split()]
    matrix.append(tmp)
    

for i in range(n):
    for q in range(n):
        print(matrix[q][i], end=" ")
    print()



