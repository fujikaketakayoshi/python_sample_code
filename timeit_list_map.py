import timeit

print(timeit.timeit("[str(x) for x in range(10000)]", number=10000))
print(timeit.timeit("list(map(str, range(10000)))", number=10000))
