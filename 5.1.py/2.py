
n=int(input())
matrix=[]
for k in range(n):
    tmp=[int(x) for x in input().split()]
    matrix.append(tmp)
    
    
Max=matrix[0][0]
for i in range(n):
    for q in range(n):
        if i >= n - 1 - q and matrix[i][q] > Max:
            Max=matrix[i][q]
print(Max)



