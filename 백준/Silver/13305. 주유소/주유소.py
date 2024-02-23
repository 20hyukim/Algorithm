len_city = int(input())
d = list(map(int, input().split()))
city = list(map(int, input().split()))

city_w_index = [[money, city_num] for city_num, money in enumerate(city)]
#print(city_w_index)
city_w_index.sort()
#print(city_w_index)

visited = [False]*(len_city+1)
total = 0

for m, c in city_w_index:
    if visited[c]:
        continue
    for i in range (c+1, len(city), 1):
        if not visited[i]:
            total += d[i-1] * m
            visited[i] = True

print(total)