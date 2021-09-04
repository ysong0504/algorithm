# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!

# 1. 시작 노드를 큐에 넣는다
# 2. 현재 큐의 노드를 빼서 visited 에 추가
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않는 노드를 큐에 추가
# 4. 2,3번 과정을 큐가 빌 때까지 진행한다.

from collections import deque

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    queue = deque([start_node])
    # queue = [start_node]
    visited = []

    while queue:
        cur_node = queue.popleft()
        # cur_node = queue.pop(0)
        visited.append(cur_node)

        for adj_node in adj_graph[cur_node]:
            if adj_node not in visited:
                queue.append(adj_node)

    # 구현해보세요!
    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!