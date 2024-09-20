from collections import defaultdict


def count_city():
    queue = [x]
    visited = [False] * (n+1)
    visited[x] = True

    for i in range(k):
        length = len(queue)

        for _ in range(length):
            q = queue.pop(0)

            for r in road[q]:
                if not visited[r]:
                    queue.append(r)
                    visited[r] = True

    if not queue:
        print(-1)
    else:
        queue.sort()
        for q in queue:
            print(q)


if __name__ == "__main__":
    road = defaultdict(list)
    n, m, k, x = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
        road[u].append(v)

    count_city()