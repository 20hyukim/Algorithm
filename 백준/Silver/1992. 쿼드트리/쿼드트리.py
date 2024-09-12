
def compress(l, r, u, d, square, n):
    summed = 0
    for i in range(u, d, 1):
        for j in range(l, r, 1):
         #   print("i:", i)
          #  print("j:", j)
            summed += square[i][j]

  #  print("summed")
   # print(summed)
   # print("n")
   # print(n)
    #print()

    if summed == 0:
        return '0'

    if summed == n**2:
        return '1'

    width_mid = (l+r)//2
    height_mid = (u+d)//2
    first = compress(l, width_mid, u, height_mid, square, n//2)
    second = compress(width_mid, r, u, height_mid, square, n//2)
    third = compress(l, width_mid, height_mid, d, square, n//2)
    fourth = compress(width_mid, r, height_mid, d, square, n//2)

    #print('('+first+second+third+fourth+')')
    return '('+first+second+third+fourth+')'


if __name__ == "__main__":
    n = int(input())
    square = []
    for _ in range(n):
        s = list(map(int, input()))
        square.append(s)

    print(compress(0, n, 0, n, square, n))