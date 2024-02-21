
n = int(input())
matrix = []
for k in range(n):
    temp = [int(x) for x in input().split()]
    matrix.append(temp)
max=matrix[0][0]
for i in range(n):
    for q in range(n):
        if (i >= q and i <= n-1-q or i<=q and i >= n -1-q) and matrix[i][q] >max:
            max=matrix[i][q]
print(max)



