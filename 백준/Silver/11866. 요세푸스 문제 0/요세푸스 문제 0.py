def que(n, k):
    ans = []
    queue = [i for i in range(1, n+1, 1)]
    count = -1
    while queue:
        count += 1
        if count == k:
            ans.append(queue.pop())
            count = -1
        else:
            queue.append(queue.pop(0))

    print(f"<{', '.join(map(str, ans))}>")


if __name__ == "__main__":
    n, k = map(int, input().split())
    que(n, k)