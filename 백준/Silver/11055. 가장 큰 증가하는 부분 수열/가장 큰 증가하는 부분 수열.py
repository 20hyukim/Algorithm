import copy

def max_val(arr, inc_a, n):
    for i in range(1, n, 1):
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                inc_a[i] = max(inc_a[i], inc_a[j] + arr[i])
                
    return max(inc_a)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    inc_a = copy.deepcopy(arr)
    print(max_val(arr, inc_a, n))