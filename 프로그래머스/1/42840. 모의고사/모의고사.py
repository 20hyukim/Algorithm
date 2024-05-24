def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    length = len(answers)

    one = one[:length]
    two = two[:length]
    three = three[:length]

    dict_a = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):
        if one[i] == answers[i]:
            dict_a[1] += 1
        if two[i] == answers[i]:
            dict_a[2] += 1
        if three[i] == answers[i]:
            dict_a[3] += 1

    sorted_keys = sorted(dict_a, key=lambda x: (-dict_a[x], x))

    count = 0

    value = dict_a[sorted_keys[0]]
    for i in range(1, 3):
        if dict_a[sorted_keys[i]] != value:
            break
        count += 1

    answer = sorted_keys[:count + 1]

    return answer