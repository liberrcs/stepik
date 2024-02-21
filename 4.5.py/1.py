
n=int(input())
m=int(input())

matrix=[[str(i*j).ljust(3)for i in range(m)] for j in range(n)]
[print(*i) for i in matrix]


