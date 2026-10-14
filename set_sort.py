arr =[1, 5, 6, 3, 2,]

seen = set(arr)

print(seen)
for i in seen:
    print(i)

seen.add(4)

print(seen)
for i in seen:
    print(i)
