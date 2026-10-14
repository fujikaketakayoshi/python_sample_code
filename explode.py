input = '5 10'
a, b = map(int, input.split())
print(a, b)

b = b // 2
print(b)


input = '5 ab cdno'
values = [int(x) if x.isdigit() else x for x in input.split()]
print(values)


input = [1, 2, 3]
values = [str(x) for x in input]
values2 = list(map(str, range(1, 6)))
print(values, values2)
