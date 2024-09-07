def make_replicated_array(num_arr):
    n = int(num_arr[0])
    arr = num_arr[1]
    d_arr = ""
    for a in arr:
        d_arr += a * n
    return d_arr


def total_arr(n):
    for i in range(n):
        print(make_replicated_array(input().split()))


if __name__ == "__main__":
    total_arr(int(input()))