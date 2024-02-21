
n = int(input())
matrix = []
for k in range(n):
    temp = [int(x) for x in input().split()]
    matrix.append(temp)
sum1=0
sum2=0
sum3=0
sum4=0
for i in range(n):
    for q in range(n):
        if i<q and i < n - 1 - q:
            sum1+=matrix[i][q]
        elif i<q and i>n-1-q:
            sum2+=matrix[i][q]
        elif i>q and i > n-1-q:
            sum3+=matrix[i][q]
        elif i > q and i < n-1-q:
            sum4+=matrix[i][q]
print(f'Верхняя четверть: {sum1}')
print(f'Правая четверть: {sum2}')
print(f'Нижняя четверть: {sum3}')
print(f'Левая четверть: {sum4}')