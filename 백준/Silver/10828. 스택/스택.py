def push(stack, n):
    stack.append(n)

    return stack

def pop(stack):
    if not stack:
        return -1

    return stack.pop()

def size(stack):
    return len(stack)


def empty(stack):
    if stack:
        return 0
    return 1

def top(stack):
    if empty(stack):
        return -1

    return stack[-1]


if __name__ == "__main__":
    stack = []

    for i in range(int(input())):
        #print(stack)
        input_stack = list(input().split())

        if input_stack[0] == "push":
            stack = push(stack, input_stack[1])

        elif input_stack[0] == "top":
            print(top(stack))

        elif input_stack[0] == "size":
            print(size(stack))

        elif input_stack[0] == "empty":
            print(empty(stack))

        else:
            print(pop(stack))