from bisect import bisect_left

def lis_length(nums):
    tails = []

    for x in nums:
        i = bisect_left(tails, x)

        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x

    return len(tails)

nums = [2, 1, 5, 0, 4, 6, 3, 7, 8, 9]
print(lis_length(nums))
