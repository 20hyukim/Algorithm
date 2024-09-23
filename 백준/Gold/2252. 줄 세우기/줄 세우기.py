from collections import deque



def topological():
    queue = deque()
    result = []
    for i in range(1, num+1, 1):
        if inD[i] == 0:
            queue.append(i)

    for _ in range(num):
        if not queue:
            return -1

        q = queue.popleft()
        result.append(q)
        for i in adj[q]:
            inD[i] -= 1
            if inD[i] == 0:
                queue.append(i)

    return " ".join(map(str, result))






if __name__ == "__main__":
    num, compare_cnt = map(int, input().split())
    adj = [[] for i in range(num+1)]
    inD = [0] * (num+1)

    for _ in range(compare_cnt):
        f, l = map(int, input().split())
        adj[f].append(l)
        inD[l] += 1

    print(topological())

