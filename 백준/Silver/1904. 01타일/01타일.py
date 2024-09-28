def fibo1(n, save):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    b1 = 1
    b2 = 2
    result =3
    for i in range(3, n+1, 1):
        result = (b1 + b2) % 15746
        b1 = b2
        b2 = result

    return result % 15746


if __name__ == "__main__":
    n = int(input())
    save = [-1] * (n+1)
    print(fibo1(n, save))