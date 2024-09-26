def count_tree_x(i, j):
    patt = pattern[i][j]
    visited[i][j] = True
    for k in range(j+1, y, 1):
        if pattern[i][k] == '-':
            visited[i][k] = True
        else:
            return 1

    return 1

def count_tree_y(i, j):
    patt = pattern[i][j]
    visited[i][j] = True
    for k in range(i+1, x, 1):
        if pattern[k][j] == '|':
            visited[k][j] = True
        else:
            return 1

    return 1



def count_trees():
    total_tree = 0
    for i in range(x):
        for j in range(y):
            if not visited[i][j]:
                if pattern[i][j] == '-':
                    total_tree += count_tree_x(i, j)
                else:
                    total_tree += count_tree_y(i, j)
    return total_tree


if __name__ == "__main__":
    x, y = map(int, input().split())
    visited = [[False] * y for _ in range(x)]
    #print(visited)
    pattern = []
    for t in range(x):
        p = list(input())
        pattern.append(p)

    print(count_trees())

