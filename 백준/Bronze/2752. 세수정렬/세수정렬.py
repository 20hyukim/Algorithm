a, b, c = map(int, input().split())
lists = [a, b, c]
lists.sort()
result = ' '.join(map(lambda x: str(x), lists))
print(result)
