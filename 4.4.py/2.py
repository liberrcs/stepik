

n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for i in range(n)]
 
for i in matrix:
    print(*i)

print()

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()


