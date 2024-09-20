from collections import deque

class Glacier:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.glacier_h = []
        self.base_sea = [[0] * m for _ in range(n)]
        self.glacier_loc = deque()
        self.total_ice = 0
        self.all_melted = False

    def set_base_sea(self, i, j):
        near_sea = 0
        if self.glacier_h[i-1][j] <= 0:
            near_sea += 1
        if self.glacier_h[i+1][j] <= 0:
            near_sea += 1
        if self.glacier_h[i][j-1] <= 0:
            near_sea += 1
        if self.glacier_h[i][j+1] <= 0:
            near_sea += 1

        return near_sea

    def set_glacier_h(self):
        for _ in range(self.n):
            self.glacier_h.append(list(map(int, input().split())))

        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if self.glacier_h[i][j] > 0:
                    self.total_ice += 1
                    self.glacier_loc.append([i, j])
                    self.base_sea[i][j] = self.set_base_sea(i, j)

    def renew_sea_status(self, popped):
        while popped:
            x, y = popped.popleft()
            self.base_sea[x-1][y] += 1
            self.base_sea[x+1][y] += 1
            self.base_sea[x][y+1] += 1
            self.base_sea[x][y-1] += 1

    def dfs(self, i, j, visited):
        stack = [(i, j)]
        count = 0
        while stack:
            x, y = stack.pop()
            if x <= 0 or x >= self.n-1 or y <= 0 or y >= self.m-1 or visited[x][y] or self.glacier_h[x][y] <= 0:
                continue
            visited[x][y] = True
            count += 1
            stack.append((x - 1, y))
            stack.append((x + 1, y))
            stack.append((x, y - 1))
            stack.append((x, y + 1))
        return count

    def check_status(self):
        if not self.glacier_loc:
            self.all_melted = True
            return False

        i, j = self.glacier_loc[0]
        visited = [[False] * self.m for i in range(self.n)]
        #print(visited)
        glacier_size = self.dfs(i, j, visited)
        if glacier_size != self.total_ice:
            return False
        return True

    def get_years(self):
        years = 0
        while self.total_ice > 0:
            years += 1
            popped_ice = deque()
            ice_length = len(self.glacier_loc)
            for _ in range(ice_length):
                i, j = self.glacier_loc.popleft()
                self.glacier_h[i][j] -= self.base_sea[i][j]
                if self.glacier_h[i][j] <= 0:
                    popped_ice.append([i, j])
                    self.total_ice -= 1
                else:
                    self.glacier_loc.append([i, j])

            self.renew_sea_status(popped_ice)
            if not self.check_status():
                if self.all_melted:
                    return 0
                return years

        return 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    glacier = Glacier(n, m)
    glacier.set_glacier_h()
    print(glacier.get_years())