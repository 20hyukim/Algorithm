from collections import Counter

lists = []
for i in range(10):
    lists.append(int(input()))
counter = Counter(lists)
print(int(sum(lists)/10))
print(counter.most_common(1)[0][0])