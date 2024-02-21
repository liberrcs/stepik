n = int(input())
matrix = []
for _ in range(n):
    temp = [0 for e in range(n)]
    matrix.append(temp)

for i in range(n):
    for q in range(n):
        if i == q:
            matrix[i][q] = 1
        elif i == n - 1 - q:
            matrix[i][q] = 1

for i in range(n):
    print(*matrix[i])
            
            