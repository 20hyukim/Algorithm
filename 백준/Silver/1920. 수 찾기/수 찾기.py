from collections import defaultdict


def make_dict(has_it):
    dict_n = defaultdict(lambda: 0)
    for n in has_it:
        dict_n[n] = 1

    return dict_n


def compare_each(dict_c, c):
    if dict_c[c]:
        return 1
    return 0


def compare():
    input()
    has_it = list(map(int, input().split()))
    input()
    compare_to = list(map(int, input().split()))
    dict_c = make_dict(has_it)

    for c in compare_to:
        print(compare_each(dict_c, c))


if __name__ == "__main__":
    compare()
