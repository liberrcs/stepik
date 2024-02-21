n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)



for i in range(n):
    sum=0
    count=0
    for q in range(n):
        sum+=matrix[i][q]
    for r in range(n):
        if matrix[i][r] > sum / n:
            count +=1
    print(count)