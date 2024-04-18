s=input().lower().split()

x=[word.strip("[.,;:-?-!") for word in s]

mydict={}
for i in x:
    mydict[i] = x.count(i)
result={}
min_count=min(mydict.values())
for key, value in mydict.items():
    if value == min_count:
        result[key] = value
print(min(result)) 