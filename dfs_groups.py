N = 4
groups = []

def dfs(i):
    if i == N:
        print(groups)
        return

    # 既存グループに入れる
    for j in range(len(groups)):
        groups[j].append(i)
        dfs(i + 1)
        groups[j].pop()

    # 新規グループ
    groups.append([i])
    dfs(i + 1)
    groups.pop()

dfs(0)
