import queue

def get_info(y):
    paint = []
    for _ in range(y):
        p = list(map(int, input().split()))
        paint.append(p)

    return paint

def print_paint(paint):
    for p in paint:
        print(p)
    print()
    print()

def paint_size(i, j):
    q = queue.Queue()
    q.put((i, j))
    udlf = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    count = 1
    while not q.empty():
        q_i, q_j = q.get()
        #print(q_i, q_j)
        for a, b in udlf:
            if 0 <= q_i+a < y and 0 <= q_j+b < x and paint[q_i+a][q_j+b] == 1:
                paint[q_i + a][q_j + b] = 0
                #print_paint(paint)
                count += 1
                q.put((q_i+a, q_j+b))

    return count


if __name__ == "__main__":
    y, x = map(int, input().split())
    paint = get_info(y)
    paint_count = 0
    max_size = 0
    for i in range(y):
        for j in range(x):
            if paint[i][j] == 1:
                paint[i][j] = 0
                paint_count += 1
                paint_s = paint_size(i, j)
                if max_size < paint_s:
                    max_size = paint_s

    print(paint_count)
    print(max_size)