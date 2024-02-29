list=[]
n=int(input())
w=input()
for i in range(n):
    list.append(len(set(w).lower))
print(*list, sep ="\n")