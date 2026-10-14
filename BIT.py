A = [1, 2, 8, 4, 5, 6, 7, 3]

# ---- 座標圧縮 ----
vals = sorted(set(A))
comp = {v: i for i, v in enumerate(vals)}

# ---- Fenwick Tree ----
size = len(vals)
bit = [0] * (size + 1)

def add(i, x):
    i += 1
    while i <= size:
        bit[i] += x
        i += i & -i
        print(bit)

def sum_(i):
    s = 0
    i += 1
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

# ---- main ----
ans = 0
for x in A:
    idx = comp[x]
    ans += sum_(idx - 1)  # 自分より小さいもの
    print(x, idx)
    add(idx, 1)

print(ans)
