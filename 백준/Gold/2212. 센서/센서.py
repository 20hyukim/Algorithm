
sensor_len = int(input())
k = int(input())

sensors = set(map(int, input().split()))
sensor = list(sensors)
sensor.sort()

dff = []
for i in range(len(sensor)-1):
    dff.append(sensor[i+1] - sensor[i])

dff_sorted = dff.copy()
dff_sorted.sort(reverse=True)

for i in range(k-1):
    if dff_sorted:
        max_d = dff_sorted.pop(0)


print(sum(dff_sorted))
