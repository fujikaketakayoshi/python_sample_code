from sortedcontainers import SortedSet

ss = SortedSet([1, 3, 5, 7, 9])
ss.add(18)
ss.remove(5)
ss.discard(9)
print(ss)

l = ss.bisect_left(3)
r = ss.bisect_right(7)

print(list(ss)[l:r])