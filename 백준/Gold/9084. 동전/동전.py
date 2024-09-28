

def count_coin(total, i, n, c_dict, coin_values):
    if total < 0:
        return 0
    if c_dict.get((i, total)):
        return c_dict[(i, total)]
    if i == n-1:
        if total%coin_values[i] == 0:
            return 1
        return 0

    sub_sum = 0
    quo = total//coin_values[i]
    for q in range(quo + 1):
        sub_sum += count_coin(total - q*coin_values[i], i+1, n, c_dict, coin_values)

    c_dict[(i, total)] = sub_sum
    return c_dict[(i, total)]
def count_coins():
    global cnt
    coin_num = int(input())
    coin_values = list(map(int, input().split()))
    coin_values.sort(reverse=True)
    money = int(input())
    #cnt = 0
    c_dict = {}
    print(count_coin(money, 0, coin_num, {}, coin_values))
    #print(cnt)


if __name__ == "__main__":
    repeat = int(input())
    for _ in range(repeat):
        count_coins()