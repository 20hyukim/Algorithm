def DFS(rows, m):
    if len(rows) == m:
        print(' '.join(map(str, rows)))
        return
    for i in range(1, n + 1, 1):
        if len(rows) == 0 or rows[-1] < i:
            DFS(rows + [i], m)


n, m = map(int, input().split())
DFS([], m)
