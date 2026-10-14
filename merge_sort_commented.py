from typing import List

def merge_sort(arr: List[int], depth=0) -> List[int]:
    indent = "  " * depth

    print(f"{indent}in {arr}")

    if len(arr) <= 1:
        print(f"{indent}out {arr}")
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    print(f"{indent}left: {left}, right: {right}")

    res = []
    i = j = 0

    while i < len(left) and j < len(right):

        print(f"{indent}compare: {left[i]} and {right[j]}")

        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

        print(f"{indent}res = {res}")

    # 残りを追加
    if i < len(left):
        print(f"{indent}left残り追加: {left[i:]}")
    if j < len(right):
        print(f"{indent}right残り追加: {right[j:]}")

    res.extend(left[i:])
    res.extend(right[j:])

    print(f"{indent}out {res}")
    return res


arr = merge_sort([5, 2, 9, 1, 5, 6])
print("result:", arr)