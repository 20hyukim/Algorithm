dict_t = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3}


def triangle(x):
    if x in dict_t:
        return dict_t[x]
    dict_t[x] = triangle(x - 2) + triangle(x - 3)
    return dict_t[x]


for i in range(int(input())):
    print(triangle(int(input())))
