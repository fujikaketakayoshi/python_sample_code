from bisect import bisect_left

def lis(nums):
    n = len(nums)

    # tails: 長さi+1のLISの末尾の値
    tails = []

    # tails_idx[i]:
    # 長さi+1のLISの末尾となっている元配列のインデックス
    tails_idx = []

    # prev[i]:
    # nums[i]の1つ前の要素のインデックス
    prev = [-1] * n

    for i, x in enumerate(nums):
        pos = bisect_left(tails, x)

        if pos == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[pos] = x
            tails_idx[pos] = i

        # 長さ2以上なら直前を記録
        if pos > 0:
            prev[i] = tails_idx[pos - 1]

    # 復元
    ans = []
    idx = tails_idx[-1]

    while idx != -1:
        ans.append(nums[idx])
        idx = prev[idx]

    ans.reverse()
    return ans


nums = [2, 1, 5, 0, 4, 6, 3, 7, 8, 9]

print(lis(nums))