import heapq

hq = []  # 空のヒープを作る

heapq.heappush(hq, 5)
heapq.heappush(hq, 3)
heapq.heappush(hq, 7)
heapq.heappush(hq, 1)

print(hq)

x = heapq.heappop(hq)
print(x)
x = heapq.heappop(hq)
print(x)
x = heapq.heappop(hq)
print(x)


hq = []
heapq.heappush(hq, (1, 2))
heapq.heappush(hq, (3, 4))
heapq.heappush(hq, (1, 5))
print(hq)
print(heapq.heappop(hq))
print(heapq.heappop(hq))
print(heapq.heappop(hq))