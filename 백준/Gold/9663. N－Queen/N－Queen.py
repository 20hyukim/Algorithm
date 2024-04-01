def is_safe(board, row, col, n):
    # 같은 열에 다른 퀸이 있는지 확인
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_n_queens(n, board=[], row=0):
    if row == n:
        return 1  # 모든 퀸을 성공적으로 배치, 1가지 방법 찾음
    count = 0
    for col in range(n):
        if is_safe(board, row, col, n):
            board.append(col)  # 퀸 배치
            count += solve_n_queens(n, board, row + 1)  # 다음 행에 대해 해결 시도
            board.pop()  # 백트래킹: 현재 행의 퀸을 제거하고 다른 위치 시도
    return count  # 현재까지 찾은 모든 유효한 방법의 수 반환


def n_queens(n):
    return solve_n_queens(n)


# 예를 들어, N = 4일 때의 해를 구하는 방법
n = int(input())
print(n_queens(n))
