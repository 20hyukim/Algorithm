def get_max_meetings(times):
    # 종료 시간 기준으로 회의를 정렬 (종료 시간이 같을 경우 시작 시간 기준으로 정렬)
    times.sort(key=lambda x: (x[1], x[0]))

    # 선택된 회의의 수와 마지막으로 선택된 회의의 종료 시간을 저장할 변수
    count = 0
    last_end_time = 0

    for start, end in times:
        # 현재 회의의 시작 시간이 마지막 회의의 종료 시간보다 크거나 같으면 선택
        if start >= last_end_time:
            count += 1  # 회의 선택
            last_end_time = end  # 마지막으로 선택된 회의의 종료 시간 업데이트

    return count

if __name__ == "__main__":
    n = int(input())  # 회의의 수 입력
    times = []
    for _ in range(n):
        s, e = map(int, input().split())
        times.append([s, e])

    print(get_max_meetings(times))