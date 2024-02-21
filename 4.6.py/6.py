
n = int(input())
matrix = []
for _ in range(n):
    temp = [0 for e in range(n)]
    matrix.append(temp)

for i in range(n):
    for q in range(n):
        if i <= q and i <= n - 1 - q:
            matrix[i][q] = 1
        elif i >= q and i >= n - 1 - q:
            matrix[i][q] = 1

for i in range(n):
    for q in range(n):
         print(str(matrix[i][q]).ljust(3), end=" ")
    print()
  
            



