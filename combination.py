nums = [1,2,3,4]
def combination(arr, r):
    results = []
    def dfs(path, start):
        if len(path) == r:
            results.append(tuple(path[:]))
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(path, i + 1)
            path.pop()
    dfs([], 0)
    return results
print(combination(nums, 3))

import itertools
print(list(itertools.combinations(nums, 4)))