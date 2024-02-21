
x,y=input()
n=8
matrix=[["."] * n for _ in range(n)]
y=n-int(y)
x=ord(x)-97
matrix[y][x] = "N"
for i in range(n):
    for q in range(n):
        if abs(i-y) * abs(q-x) == 2:
            matrix[i][q]="*"
for x in range(n):
    print(*matrix[x])
            



