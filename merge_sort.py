def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    res = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    # 残りを追加
    res.extend(left[i:])
    res.extend(right[j:])

    return res


arr = merge_sort([5, 2, 9, 1, 5, 6])
print(arr)