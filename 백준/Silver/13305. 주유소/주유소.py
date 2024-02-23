len_city = int(input())
d = list(map(int, input().split()))
city = list(map(int, input().split()))
visited_city = []
total = 0
for i in range(0, len_city-1, 1):
    visited_city.append(city[i])
    total += d[i] * min(visited_city)

print(total)