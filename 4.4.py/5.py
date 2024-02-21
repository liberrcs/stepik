n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

max=matrix[0][0]
for i in range(n):
    for q in range(n):
        if i >= q and matrix[i][q] > max:
            max=matrix[i][q]
print(max)





