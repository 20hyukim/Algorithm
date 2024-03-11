import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

q = math.ceil(a / c)
w = math.ceil(b / d)

print(l - max(q, w))
