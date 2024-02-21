
x=input().split()
n,m = int(x[0]), int(x[1])
matrix=[]
for _ in range(n):   
    tmp=[i for i in range(1, m + 1)]
    matrix.append(tmp)

count=1 
for i in range(n):
    for q in range(m):
        matrix[i][q] = count
        count += 1
        
for i in range(n):
    if i % 2 != 0:
        matrix[i].reverse()

for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end=" ")
    print()
 

