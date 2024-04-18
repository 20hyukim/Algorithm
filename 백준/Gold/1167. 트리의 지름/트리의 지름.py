import sys

sys.setrecursionlimit(10000)


def dfs(node, visited, distance):
    visited.add(node)
    farthest_node = node
    max_distance = distance
    for neighbor, weight in nodes[node]:
        if neighbor not in visited:
            candidate_node, candidate_distance = dfs(neighbor, visited, distance + weight)
            if candidate_distance > max_distance:
                farthest_node = candidate_node
                max_distance = candidate_distance
    visited.remove(node)
    return farthest_node, max_distance


n = int(input())  # 노드의 수
nodes = [[] for _ in range(n + 1)]  # 인접 리스트 초기화

for _ in range(n):
    node_list = list(map(int, input().split()))
    for i in range(1, len(node_list) - 1, 2):
        if node_list[i] == -1:
            break
        nodes[node_list[0]].append((node_list[i], node_list[i + 1]))

# 1번 노드부터 시작하여 가장 먼 노드 찾기
farthest, _ = dfs(1, set(), 0)

# 찾은 노드에서 다시 DFS를 수행하여 최대 거리 찾기
_, max_length = dfs(farthest, set(), 0)

print(max_length)
