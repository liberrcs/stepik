
x=input().split()
n,m = int(x[0]), int(x[1])
tmp=[i for i in range(1, m + 1)]
matrix=[]

for i in range(n):
    matrix.append(tmp)
    tmp = tmp[1:] + [tmp[0]]
    
for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end =" ")
    print()



