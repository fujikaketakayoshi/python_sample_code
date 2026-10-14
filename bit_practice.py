N = 10
print(bin(0 << N))
print(bin(1 << N))
print(bin(2 << N))
print(bin(N), bin(N >> 1))

for S in range(1 << N):
    idx = []
    for i in range(N):
        if (S >> i) & 1:
            # print(i, bin(S >> i), (S >> i) & 1)
            idx.append(i)
    # print(f'S={S:0{N}b}, idx={idx}')