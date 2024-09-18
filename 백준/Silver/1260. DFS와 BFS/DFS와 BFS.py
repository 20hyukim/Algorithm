from collections import defaultdict


def bfs(start):
    queue = [start]
    answer = []
    visited = [False] * (n + 1)
    while queue and len(answer) != n:
        i = queue.pop(0)
        visited[i] = True
        answer.append(i)

        i_list = sorted(dict_n[i])
        for i_near in i_list:
            if not visited[i_near] and i_near not in queue:
                queue.append(i_near)

    return " ".join(map(str, answer))


def dfs(cur_index, visited):
    if len(answer) == n:
        return
    visited[cur_index] = True
    answer.append(cur_index)
    i_list = sorted(dict_n[cur_index])

    for i in i_list:
        if not visited[i]:
            dfs(i, visited)


if __name__ == "__main__":
    n, m, start = map(int, input().split())
    dict_n = defaultdict(list)
    duplicated = set()
    for i in range(m):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        duplicated.add((x, y))

    for x, y in duplicated:
        dict_n[x].append(y)
        dict_n[y].append(x)

    answer = []
    visited = [False] * (n + 1)
    dfs(start, visited)
    #print(answer)
    print(" ".join(map(str, answer)))
    print(bfs(start))
