def compute(b_stack):
    a_stack = []

    while b_stack:
        popped = b_stack.pop()

        if popped == ')' or popped == ']':
            a_stack.append(popped)

        else:
            if popped == '[' and a_stack and a_stack[-1] == ']':
                a_stack.pop()
                a_stack.append(3)

            elif popped == '(' and a_stack and a_stack[-1] == ')':
                a_stack.pop()
                a_stack.append(2)

            elif a_stack and isinstance(a_stack[-1], int):
                nums = [a_stack.pop()]

                while a_stack and isinstance(a_stack[-1], int):
                    nums.append(a_stack.pop())

                if a_stack and a_stack[-1] == ')' and popped == '(':
                    a_stack.pop()
                    a_stack.append(2*sum(nums))

                elif a_stack and a_stack[-1] == ']' and popped == '[':
                    a_stack.pop()
                    a_stack.append(3*sum(nums))
                else:
                    return 0

            else:
                return 0

    for s in a_stack:
        if not isinstance(s, int):
            return 0

    return sum(a_stack)


if __name__ == "__main__":
    b_stack = list(input())
    print(compute(b_stack))
