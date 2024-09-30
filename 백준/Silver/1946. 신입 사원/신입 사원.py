
def max_employee():
    n = int(input())
    applies = []
    for _ in range(n):
        apply = list(map(int, input().split()))
        applies.append(apply)
    applies.sort()

    second_max_s = applies[0][1]
    cnt = 1

    for i in range(1, n, 1):
        if second_max_s > applies[i][1]:
            cnt += 1
            second_max_s = applies[i][1]

    return cnt


if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        print(max_employee())