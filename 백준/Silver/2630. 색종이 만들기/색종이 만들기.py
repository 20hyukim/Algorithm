blue = 0
white = 0


def make_origami(n):
    origami = []
    for i in range(n):
        ori = list(map(int, input().split()))
        origami.append(ori)

    return n, origami


def count_blue_white(left, right, up, down, origami, n):
    global blue
    global white

    summed = 0

    for i in range(up, down, 1):
        for j in range(left, right, 1):
            summed += origami[i][j]

    if summed == n**2:
        blue += 1
        return

    elif summed == 0:
        white += 1
        return

    else:
        width_mid = int((left + right)/2)
        height_mid = int((up + down)/2)
        n = int(n/2)

        count_blue_white(left, width_mid, up, height_mid, origami, n)
        count_blue_white(width_mid, right, up, height_mid, origami, n)
        count_blue_white(left, width_mid, height_mid, down, origami, n)
        count_blue_white(width_mid, right, height_mid, down, origami, n)


if __name__ == "__main__":
    n, origami = make_origami(int(input()))
    count_blue_white(0, n, 0, n, origami, n)
    print(white)
    print(blue)