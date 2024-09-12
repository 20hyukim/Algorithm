def make_two(n):
    return '0'+str(n)


def add_up(str_n):
    added = int(str_n[0]) + int(str_n[1])
    remainder = added % 10
    return str(remainder)


def count_cycle(n):
    orig_n = n
    new_n = n - 1
    count = 0
    while orig_n != new_n:
        count += 1
        if n < 10:
            str_n = make_two(n)
        else:
            str_n = str(n)

        n = str_n[1] + add_up(str_n)
        new_n = int(n)
        n = int(n)

    return count


if __name__ == "__main__":
    n = int(input())
    print(count_cycle(n))