items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
myset=set()
for i in items:
    myset.add(int(i))
print(*sorted(myset))



