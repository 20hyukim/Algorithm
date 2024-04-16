def available(m, i):
    count = 1
    for h in house:
        if h >= i + m:
            count += 1
            i = h
        if count >= c:
            break

    if count < c:
        return False

    return True


n, c = map(int, input().split())

house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

l = 0
r = house[-1]
current = 0
while l <= r:
    m = (l + r) // 2

    if available(m, house[0]):
        l = m + 1
        current = m
    else:
        r = m - 1

print(current)
