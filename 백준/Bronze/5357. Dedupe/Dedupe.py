n = int(input())

for i in range(n):
    l = input()
    result = l[0]
    c = l[0]
    for a in l[1:]:
        if c != a:
            result += a
            c = a
    print(result)
