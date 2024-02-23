import heapq


def input_schedule():
    total = []

    for i in range(int(input())):
        total.append(list(map(int, input().split())))
    total.sort()

    return total


def min_rooms(total):
    rooms = 0
    end_times = []
    for start, end in total:
        if end_times and end_times[0] <= start:
            heapq.heappop(end_times)
            heapq.heappush(end_times, end)
        else:
            heapq.heappush(end_times, end)
            rooms += 1

    return rooms


def main():
    total_schedule = input_schedule()
    print(min_rooms(total_schedule))


if __name__ == "__main__":
    main()