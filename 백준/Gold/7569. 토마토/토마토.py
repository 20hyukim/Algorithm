from collections import deque


# 3차원 BFS를 통해 토마토가 모두 익는 시간을 구하는 함수
def get_years(arr, stack, not_riped_cnt, x, y, z):
    # 상하좌우, 위아래 6방향을 표현
    directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    year = 0

    while stack and not_riped_cnt > 0:
        length = len(stack)
        for _ in range(length):
            s_z, s_y, s_x = stack.popleft()

            # 6방향 탐색
            for dz, dy, dx in directions:
                nz, ny, nx = s_z + dz, s_y + dy, s_x + dx

                # 범위를 벗어나는 경우 제외
                if not (0 <= nz < z and 0 <= ny < y and 0 <= nx < x):
                    continue

                # 이미 익었거나 빈 공간이 아닌 경우 제외
                if arr[nz][ny][nx] != 0:
                    continue

                # 토마토가 익음
                arr[nz][ny][nx] = 1
                stack.append((nz, ny, nx))
                not_riped_cnt -= 1

        year += 1

    # 익지 않은 토마토가 남아 있으면 -1 리턴
    if not_riped_cnt > 0:
        return -1
    return year


if __name__ == "__main__":
    x, y, z = map(int, input().split())

    # 3차원 배열을 리스트로 초기화
    arr = [[[0 for _ in range(x)] for _ in range(y)] for _ in range(z)]

    riped = deque()
    not_riped_cnt = 0

    for i in range(z):
        for j in range(y):
            one_box = list(map(int, input().split()))
            for k in range(x):
                arr[i][j][k] = one_box[k]
                if one_box[k] == 1:
                    riped.append((i, j, k))
                elif one_box[k] == 0:
                    not_riped_cnt += 1

    # 결과 계산 및 출력
    result = get_years(arr, riped, not_riped_cnt, x, y, z)
    print(result)