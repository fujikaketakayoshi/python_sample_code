arr = [(1, 2, 3), (1, 5, 6), (1, 8, 9)]
sorted_arr = sorted(arr, key=lambda t: (t[0], -t[1], -t[2]))
print(sorted_arr)