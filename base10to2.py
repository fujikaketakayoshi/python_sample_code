num = 2 ** 10
binary = bin(num)
print(binary)

format_binary = format(num, 'b')
print(format_binary)

num2 = int(format_binary, 2)
print(num2)

binary_str = "111"
decimal = int(binary_str, 2)
print(decimal)
