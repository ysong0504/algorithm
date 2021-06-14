# 21-06-14
# 맥스 힙에 원소 추가하기

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 1. 원소를 맨 끝에 추가한다.
        # 2. 신규 노드와 부모 노드를 비교한다.
        # 3. 1과 2 과정을 꼭대기까지 반복한다.

        self.items.append(value)
        cur_idx = len(self.items) - 1

        # 힙이 비어있다면 비교없이 값 입력
        if cur_idx == 1:
            return

        while cur_idx > 1:
            parent_node_idx = cur_idx // 2

            if self.items[cur_idx] > self.items[parent_node_idx]:
                self.items[cur_idx], self.items[parent_node_idx] = self.items[parent_node_idx], self.items[cur_idx]
                cur_idx = parent_node_idx
            else:
                return




        # print(self.items)
        # 구현해보세요!
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
