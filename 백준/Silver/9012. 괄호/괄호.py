def vps(s):
    left = []
    for i in s:
        if i=='(':
            left.append(1)
        else:
            if len(left)==0:
                return "NO"
            else:
                left.pop()
        #print(left)
    if len(left)!=0:
        return "NO"
    return "YES"


n = int(input())

for i in range(n):
    str = input()
    print(vps(str))