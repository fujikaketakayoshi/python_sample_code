words = "abcw"
words2 = "abcdef"
words3 = "xyz"

set1 = set(words)
set2 = set(words2)
set3 = set(words3)

if set1.isdisjoint(set2):
    print("Yes")
else:
    print("No")

if set1.isdisjoint(set3):
    print("Yes")
else:
    print("No")