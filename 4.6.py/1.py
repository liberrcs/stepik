x=input().split()
n,m=int(x[0]), int(x[1])
matrix=[]
for _ in range(n):
    temp=[e for e in range(m)]
    matrix.append(temp)
          
for i in range(n):
    for q in range(m):
          if ( i + q) % 2 == 0:
              matrix[i][q] = "."
          else:
              matrix[i][q] = "*"

for i in range(n):
    print(*matrix[i])