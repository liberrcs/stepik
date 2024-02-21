
n=int(input())
matrix=[]
for _ in range(n):
    temp=[int(e) for e in range(n)]
    matrix.append(temp)

for i in range(n):
    for q in range(n):
        if i == n - 1 - q:
            matrix[i][q] = 1
        elif i < n - 1 - q:
            matrix[i][q] = 0 
        elif i > n - 1 - q:
            matrix[i][q] = 2
            
for i in range(n):
    print(*matrix[i])


