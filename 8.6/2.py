n = list(map(int, input().split()))
n = set(n)
n1 = list(map(int, input().split()))
n1 = set(n1)
c = n.intersection(n1)
print(*sorted(c))