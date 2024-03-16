



m=int(input())
n=int(input())
s={input() for _ in range(m)}
for i in range(n):
    if input() in s:
        print("YES")
    else:
        print("NO")
