nums = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in nums))  # → True (全部偶数)

nums = [1, 3, 5, 7]
print(any(n % 2 == 0 for n in nums))  # → True (偶数が1つでもある)


password = "abc123!"
conditions = [
    any(c.isdigit() for c in password),   # 数字を含むか
    any(c.isalpha() for c in password),   # 文字を含むか
    any(not c.isalnum() for c in password) # 記号を含むか
]
if all(conditions):
    print("強いパスワード")
else:
    print("弱いパスワード")
