def compute_score(s):
    if s >= 90:
        return 'A'
    elif s >= 80:
        return 'B'
    elif s >= 70:
        return 'C'
    elif s >= 60:
        return 'D'
    return 'F'


print(compute_score(int(input())))
