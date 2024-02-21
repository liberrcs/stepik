
x=input().split()
n,m=int(x[0]), int(x[1])
matrix=[]
for _ in range(n):
    temp=[e for e in range(m)]
    matrix.append(temp)
    
count=1
for i in range(n):
    for q in range(m):
        matrix[i][q] = count
        count += 1 

for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end=" ")
    print()



