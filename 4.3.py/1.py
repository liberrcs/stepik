n=int(input())
result=[]
for _ in range(n):
    result.append([int(q) for q in range(1, n+1)])
print(*result, sep="\n")







