import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def get_pre():
    while True:
        try:
            pre.append(int(input()))

        except:
            break


def print_post(start, end):
    if start > end:
        return
    mid = end + 1 # 오른쪽 sub tree 가 없을 때를 대비한, 설정
    for i in range(start+1, end+1):
        if pre[start] < pre[i]:
            mid = i
            break

    print_post(start+1, mid-1)
    print_post(mid, end)
    print(pre[start])


if __name__ == "__main__":
    pre = []
    get_pre()
    print_post(0, len(pre) - 1)