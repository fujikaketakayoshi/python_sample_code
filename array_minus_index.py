arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = 4
idx = arr.index(start)
arr.pop(idx)
step = 3
dir = "CW"
while arr:
    if dir == "CW":
        idx = (idx + (step - 1)) % len(arr)
    else:
        idx = (idx - (step - 1)) % len(arr)
    print(arr.pop(idx))
