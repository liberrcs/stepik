n = list(map(int, input().split()))
n = set(n)
n1 = list(map(int, input().split()))
n1 = set(n1)
n2=n.difference(n1)
print(*sorted(n2))