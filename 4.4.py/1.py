
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append([input() for _ in range(m)])
    print(*matrix[i])



