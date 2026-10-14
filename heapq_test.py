import heapq

nums = [(1, 1), (1, 3), (1, 2)]
heapq.heapify(nums)  # リストをヒープに変換
print("Heapified list:", nums)
heapq.heappush(nums, (2, 4))  # 要素をヒープに追加
print("After pushing 4:", nums)
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))
