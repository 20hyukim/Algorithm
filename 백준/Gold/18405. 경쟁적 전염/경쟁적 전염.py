def print_viruse():
    for i in range(n):
        print(viruses[i])

def colony(i, j, not_confirmed, visited):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    val = viruses[i][j]

    for l, r in directions:
        if 0<= i+l < n and 0 <= j+r < n and viruses[i+l][j+r] == 0:
            viruses[i+l][j+r] = val
            not_confirmed[i+l][j+r] = True
            visited[i+l][j+r] = True
        elif 0 <= i+l < n and 0 <= j+r < n and not_confirmed[i+l][j+r] == True:
            if viruses[i+l][j+r] > val:
                viruses[i+l][j+r] = val





def compete():
    for _ in range(s):
        not_confirmed = [[False] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if viruses[i][j] != 0 and not visited[i][j]:
                    colony(i, j, not_confirmed, visited)
        if viruses[x-1][y-1] != 0:
            return

if __name__ == "__main__":
    n, k = map(int, input().split())
    viruses = []

    for i in range(n):
        v = list(map(int, input().split()))
        viruses.append(v)

    s, x, y = map(int, input().split())
    compete()
    print(viruses[x-1][y-1])