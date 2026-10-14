def base_n(num, base):
    if num == 0:
        return "0"

    s = ""
    while num:
        s = str(num % base) + s
        num //= base

    return s

num = 3 ** 10 - 1
print(base_n(num, 3))