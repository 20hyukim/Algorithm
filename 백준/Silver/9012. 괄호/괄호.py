def vps(paren):
    stack = []
    for p in paren:
        if p =='(':
            stack.append(1)
            continue
        if not stack:
            return 'NO'
        stack.pop()

    if stack:
        return 'NO'
    return 'YES'


def main():
    for i in range(int(input())):
        print(vps(input()))


if __name__ == "__main__":
    main()
