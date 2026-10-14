nums = [1, 2, 3, 4, 5]
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for n in nums:
    found = False
    for row in arr:
        for m in row: 
            if n == m:
                found = True
                break
        if found:
            break
