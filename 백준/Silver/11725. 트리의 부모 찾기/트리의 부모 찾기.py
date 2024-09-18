from collections import defaultdict

node_len = int(input())
node_dict = defaultdict(list)

for i in range(node_len - 1):
    start, end = map(int, input().split())
    node_dict[start].append(end)
    node_dict[end].append(start)


dict = defaultdict(int)
dict[1] = 0
order = [1]
i = 0

while len(dict) != node_len:
    for node in node_dict[order[i]]:
        if node not in dict:
            order.append(node)
            dict[node] = order[i]
    i += 1

for i in range(2, node_len + 1, 1):
    print(dict[i])