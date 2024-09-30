def get_max_meetings(times):
    times.sort(key=lambda x:(x[1], x[0]))

    start = 0
    cnt = 0
    cur_end_time = 0

    for s, e in times:
        if cur_end_time <= s:
            cnt += 1
            cur_end_time = e

    return cnt


if __name__ == "__main__":
    n = int(input())
    times = []
    for _ in range(n):
        s, e = map(int, input().split())
        times.append([s, e])

    print(get_max_meetings(times))