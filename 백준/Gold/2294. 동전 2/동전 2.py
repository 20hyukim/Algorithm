import sys
from collections import deque


if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = set()
    dq = deque()

    for i in range(n):
        coins.add(int(input()))

    coins = list(coins)

    costs = [sys.maxsize] * (k+1)
    costs[0] = 0

    dq.append((0, 0))

    while dq:
        cost, n_coins = dq.popleft()

        for i in range(len(coins)):
            new_c = cost + coins[i]
            if new_c > k:
                continue
            if costs[new_c] > n_coins + 1:
                #print("if costs[%d] > n_coins %d + 1:" %(new_c, n_coins))
                #print("costs[%d] : %d" %(new_c, costs[new_c]))
                #print("cost : %d, n_coins : %d" %(cost, n_coins))
                #print("new_c : %d, n_coins : %d" %(new_c, n_coins))
                #print("costs[15] : %d" %(costs[15]))
                #print("costs[new_c] : %d, n_coins + 1 : %d" %(costs[new_c], n_coins + 1))
                costs[new_c] = n_coins + 1
                #print("costs[%d] : %d" %(new_c, costs[new_c]))
                dq.append((new_c, n_coins + 1))
                #print()
                #print()

    if costs[-1] > k:
        print(-1)
    else:
        print(costs[-1])
