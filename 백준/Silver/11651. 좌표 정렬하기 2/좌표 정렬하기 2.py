coor = []

for i in range(int(input())):
    coor.append(list(map(int, input().split())))

sorted_coor = sorted(coor, key=lambda coor: (coor[1], coor[0]))

for coor in sorted_coor:
    print(coor[0], coor[1])
