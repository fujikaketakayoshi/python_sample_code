from collections import deque

q = deque()
q.extend([1, 2, 3])
q.append(4)
q.appendleft(0)

for i in q:  # 1
    print(i)
print(q.popleft())  # 1
print(q.pop())  # 4
print(q)

dq = deque(maxlen=3)  # 最大長を指定できる
dq.extend([1, 2, 3])
dq.append(4)  # 古い要素が自動で消える → [2, 3, 4]
print(dq)