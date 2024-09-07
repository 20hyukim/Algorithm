
def hanoi(fromm, togo, bypass, n):
    if n == 1:
        print(fromm, togo)
        return

    hanoi(fromm, bypass, togo, n-1)
    print(fromm, togo)
    hanoi(bypass, togo, fromm, n-1)


def get_move_num(n):
    moved = 1
    for i in range(n-1):
        moved = 2 * moved + 1
    return moved


if __name__ == "__main__":
    n = int(input())
    print(get_move_num(n))
    if n <= 20:
        hanoi(1, 3, 2, n)