n={int(i) for i in input().split()}
m={int(i) for i in input().split()}
if n.isdisjoint(m):
    print("BAD DAY")
else:
    print(*sorted(n & m, reverse=True))