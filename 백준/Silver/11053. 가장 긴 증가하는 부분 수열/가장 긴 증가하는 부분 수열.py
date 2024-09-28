def longest(n, arr):
    result = [0] * (n)
    for i in range(len(arr)):
        max_v = 1
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                max_v = max(result[j]+1, max_v)
            else:
                continue

        result[i] = max_v

    #print(result)
    return max(result)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(longest(n, arr))