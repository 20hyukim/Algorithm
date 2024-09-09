def find_stranger():
    height = []
    for i in range(9):
        height.append(int(input()))

    min_height = min(height)

    sum_height = sum(height)

    over_height = sum_height - 100

    for h in range(min_height, over_height, 1):
        if h in height and over_height - h in height:
            height.remove(h)
            height.remove(over_height - h)
            break

    height.sort()

    for h in height:
        print(h)


if __name__ == "__main__":
    find_stranger()