result=[]
for elem in input().split():
    if result and elem in result[-1]:
        result[-1].append(elem)
    else:
        result.append([elem])
print(result)