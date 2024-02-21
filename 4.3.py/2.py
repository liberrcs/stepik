
n=int(input())
result=[]
for i in range(1,n+1):
    result.append([q for q in range(1, i + 1)])
print(*result, sep="\n")




