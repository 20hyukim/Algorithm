def fibo1(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fibo1(n-1) + fibo1(n-2)

def fibo2(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    before = 1
    summed = 2
    for i in range(3, n, 1):
        new_n = before + summed
        before = summed
        summed = new_n

    return summed


n = int(input())
print(fibo2(n))
