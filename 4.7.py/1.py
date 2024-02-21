x=input().split()
n,m = int(x[0]), int(x[1])
matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
z=input()
matrix2 = [[int(x) for x in input().split()] for _ in range(n)]
matrix3= [[int(x) for x in range(m)] for _ in range(n)]
for i in range(n):
    for q in range(m):
        matrix3[i][q] = matrix1[i][q] + matrix2[i][q]

for i in range(n):
    print(*matrix3[i])