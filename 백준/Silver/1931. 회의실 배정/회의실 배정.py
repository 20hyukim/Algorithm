def get_max_meetings(times):
    times.sort(key=lambda x: (x[1], x[0]))
    #print(times)

    count = 0
    last_end_time = 0

    for start, end in times:
        if start >= last_end_time:
            count += 1
            last_end_time = end

    return count

if __name__ == "__main__":
    n = int(input())
    times = []
    for _ in range(n):
        s, e = map(int, input().split())
        times.append([s, e])

    print(get_max_meetings(times))