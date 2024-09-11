from collections import deque
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    queue = deque()
    for i in range(n):
        inputs = sys.stdin.readline().split()
        if inputs[0] == "push":
            queue.append(inputs[1])

        elif inputs[0] == "pop":
            if not queue:
                print(-1)
            else:
                print(queue.popleft())

        elif inputs[0] == "size":
            print(len(queue))

        elif inputs[0] == "empty":
            if queue:
                print(0)
            else:
                print(1)

        elif inputs[0] == "front":
            if not queue:
                print(-1)
            else:
                print(queue[0])

        elif inputs[0] == "back":
            if not queue:
                print(-1)
            else:
                print(queue[-1])


