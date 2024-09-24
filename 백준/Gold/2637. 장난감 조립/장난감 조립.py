from collections import deque
from collections import defaultdict
def machine():
    dq = deque()
    base = []
    not_base = []

    for i in range(1, n+1, 1):
        if in_degree[i] == 0:
            dq.append(i)
            base.append(i)
        else:
            not_base.append(i)

    for b in base:
        part_need[b][b] = 1


    result = []
    for _ in range(n):

        #print()
        #print()
        #print("part_need: ")
        #for i in range(1, n + 1, 1):
        #    print(part_need[i])


        new_i = dq.popleft()
        result.append(new_i)

        for i, k in adj[new_i]:
            in_degree[i] -= 1

            for j in range(1, n+1, 1):
                part_need[i][j] += part_need[new_i][j] * k

            if in_degree[i] == 0:
                dq.append(i)

    for i in range(len(part_need[n])):
        if part_need[n][i] != 0:
            print("%d %d" %(i, part_need[n][i]))



if __name__ == "__main__":
    n = int(input())
    m = int(input())

    adj = [[] for i in range(n+1)]
    in_degree = [0] * (n+1)
    part_need = [[0] * (n+1) for _ in range(n+1)]

    for i in range(m):
        x, y, k = map(int, input().split())
        adj[y].append([x, k])
        in_degree[x] += 1

    #print("in_degree :", in_degree)
    #print("adj :", adj)

    machine()