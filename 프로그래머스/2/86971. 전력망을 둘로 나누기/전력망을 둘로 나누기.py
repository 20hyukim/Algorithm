from collections import defaultdict


def solution(n, wires):
    def dfs(n_dict, visited, c_node, cnt):
        for n in n_dict[c_node]:
            if not visited[n]:
                visited[n] = True
                #    print("c_node = ", c_node)
                #   print("n = ", n)
                dfs(n_dict, visited, n, cnt + 1)

    n_dict = defaultdict(list)
    least_diff = n + 1
    for x, y in wires:
        n_dict[x].append(y)
        n_dict[y].append(x)

    for x, y in wires:
        n_dict[x].remove(y)
        n_dict[y].remove(x)
        total_cnt = 0
        visited = [False] * (n + 1)
        #    print("x, y = ", x, y)
        dfs(n_dict, visited, 1, 0)
        #    print("total_cnt", total_cnt)
        n_dict[x].append(y)
        n_dict[y].append(x)

        one_diff = 0
        for v in visited:
            if v:
                one_diff += 1

        #  print("one_diff", one_diff)
        if least_diff > abs(one_diff - (n - one_diff)):
            least_diff = abs(one_diff - (n - one_diff))
    # print("least_diff", least_diff)

    return least_diff