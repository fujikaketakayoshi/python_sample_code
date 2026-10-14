A = {'a': 3, 'b': 1, 'c': 2}
sorted_A = sorted(A.items(), key=lambda x: x[1], reverse=True)
print(sorted_A)

sorted_A = sorted(A, key=A.get)
print(sorted_A)