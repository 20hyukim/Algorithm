def get_maze(x):
    maze = []
    for _ in range(x):
        m = list(input())
        maze.append(m)

    return maze

def print_visit(visited, queue):
    for _ in range(x):
        print(visited[_])
    print("queue")
    print(queue)
    print()
def get_min_cost(maze):
    visited = [[False] * y for _ in range(x)]
    visited[0][0] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = [(0, 0, 1)]
    while True:
        i, j, cost = queue.pop(0)
        if i == x-1 and j == y-1:
            return cost

        for l, r in directions:
            if 0 <= i + l < x and 0 <= j + r < y and not visited[i + l][j + r] and maze[i + l][j + r] == '1':
                visited[i + l][j + r] = True
                #print_visit(visited, queue)

                queue.append((i + l, j + r, cost + 1))


if __name__ == "__main__":
    x, y = map(int, input().split())
    maze = get_maze(x)
    print(get_min_cost(maze))
