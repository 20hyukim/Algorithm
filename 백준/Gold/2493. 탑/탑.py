def laser(n):
    hit = [0] * n
    b_shoot = []
    temp_shoot = list(map(int, input().split()))
    for i in range(len(temp_shoot)):
        b_shoot.append([temp_shoot[i], i + 1])
    a_shoot = []
    while b_shoot:
        n_h, n_i = b_shoot.pop()

        while a_shoot:
            if n_h > a_shoot[-1][0]:
                o_h, o_i = a_shoot.pop()
                hit[o_i - 1] = n_i
            else:
                break

        a_shoot.append([n_h, n_i])

    return hit


if __name__ == "__main__":
    hit = laser(int(input()))
    print(" ".join(map(str, hit)))
