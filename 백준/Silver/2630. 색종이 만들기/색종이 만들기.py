def origami(square):
    global white
    global blue
    l = len(square)
    total = sum(sum(row) for row in square)
    if total == l ** 2:
        blue += 1
        return
    if total == 0:
        white += 1
        return
    origami([row[:l // 2] for row in square[:l // 2]])
    origami([row[l // 2:] for row in square[:l // 2]])
    origami([row[:l // 2] for row in square[l // 2:]])
    origami([row[l // 2:] for row in square[l // 2:]])

    return (white, blue)


white = 0
blue = 0
nums = []
for i in range(int(input())):
    lines = list(map(int, input().split()))
    nums.append(lines)

origami(nums)
print(white)
print(blue)
