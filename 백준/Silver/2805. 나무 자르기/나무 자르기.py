def cal(trees, height, num_tree, m):
    while True:
        sum_tree = 0

        for tree in trees:
            cut = tree - height
            if cut <= 0:
                break
            sum_tree += cut

        if sum_tree >= m:
            return height
        minus = (m - sum_tree)//num_tree + 1
        if minus < 1:
            minus = 1
        height -= minus


def main():
    num_tree, m = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort(reverse=True)
    height = trees[0]

    start_point = m // len(trees)
    print(cal(trees, height - start_point, num_tree, m))


if __name__ == "__main__":
    main()