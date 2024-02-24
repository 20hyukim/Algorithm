def max_length(lines, n):
    max_line = max(lines)
    min_line = 1

    while min_line <= max_line:
        cut = (min_line + max_line) // 2
        total = 0
        for line in lines:
            total += line//cut

        if total < n:
            max_line = cut -1
        else:
            min_line = cut + 1

    return max_line


def main():
    k, n = map(int, input().split())
    lines = []

    for _ in range(k):
        lines.append(int(input()))

    print(max_length(lines, n))


if __name__ == "__main__":
    main()