# Q. 인접 리스트가 주어질 때, 모든 노드를 DFS 순서대로 방문하시오.
# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!

# 1. 시작 노드를 스택에 넣는다
# 2. 현재 스택의 노드를 빼서 visited 에 추가
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않는 노드를 스택에 추가

from collections import deque

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []

    while stack:
        cur_node = stack.pop()
        visited.append(cur_node)

        for adjacent_node in adjacent_graph[cur_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)

    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!