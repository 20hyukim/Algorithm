def sort_and_print(n):
    arr = []
    for i in range(n):
        arr.append(int(input()))

    arr.sort()

    for a in arr:
        print(a)


if __name__ == "__main__":
    sort_and_print(int(input()))