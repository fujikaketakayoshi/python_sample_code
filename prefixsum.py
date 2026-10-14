def prefix_sum(arr):
    ps = [0]
    for x in arr:
        ps.append(ps[-1] + x)
    return ps

nums = [1, 2, 3, 4, 5]
pre_sum = prefix_sum(nums)
print(pre_sum[3 + 1] - pre_sum[2])  # [0, 1, 3, 6, 10, 15]


class PrefixSum:
    def __init__(self, arr):
        self.ps = [0]
        for x in arr:
            self.ps.append(self.ps[-1] + x)

    def sum(self, l, r):
        """区間 [l, r) の和"""
        return self.ps[r + 1] - self.ps[l]

    def __getitem__(self, i):
        return self.ps[i]

    def __len__(self):
        return len(self.ps)

obj = PrefixSum(nums)
print(obj.sum(2, 3))  # 区間 [2, 4) の和

