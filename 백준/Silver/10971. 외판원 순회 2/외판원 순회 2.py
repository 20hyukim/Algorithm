routes = []
def make_array(n):
    big_arr = []
    for i in range(n):
        arr = list(map(int, input().split()))
        big_arr.append(arr)

    return big_arr


def make_possibilities(curr, not_visited):
    if not_visited == []:
        curr.append(curr[0])
        routes.append(curr)
        return

    length = len(not_visited)

    for i in range(length):
        make_possibilities(curr+[not_visited[i]],not_visited[:i]+not_visited[i+1:])

def find_min_cost(arr):
    costs = []
    for route in routes:
        cost = 0
        for i in range(len(route)-1):
            if arr[route[i]][route[i+1]] == 0:
                cost += 1000000
            cost += arr[route[i]][route[i+1]]

        costs.append(cost)

    return min(costs)


if __name__ == "__main__":
    n = int(input())
    arr = make_array(n)
    make_possibilities([0], [i for i in range(1, n, 1)])
    print(find_min_cost(arr))
