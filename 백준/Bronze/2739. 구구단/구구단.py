def multiplication_tables(n):
    for i in range(1, 10, 1):
        print("%d * %d = %d" % (n, i, n*i))
    return


multiplication_tables(int(input()))