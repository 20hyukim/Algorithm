
def cal(trees, height):
    while True:
        sum_tree = 0

        for tree in trees:
            cut = tree - height
            if cut <= 0:
                break
            sum_tree += cut

        if sum_tree >= m:
            return height
        minus = (m - sum_tree)//len(trees)
        if minus < 1:
            minus = 1
        height -= minus


num_tree, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

height = trees[0]
minus = m//len(trees)
print(cal(trees, height-minus))

