# 21-06-14
# 맥스 힙에 원소 추가하기
# 힙의 규칙
# `힙은 항상 큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있어야 합니다.`
# 은 항상 지켜져야 합니다.
#
# 따라서, 원소를 추가하거나 삭제할때도 위의 규칙이 지켜져야 합니다!
#
# 원소를 추가할 때는 다음과 같이 하시면 됩니다.
#
# 1. 원소를 맨 마지막에 넣습니다.
# 2. 그리고 부모 노드와 비교합니다. 만약 더 크다면 자리를 바꿉니다.
# 3. 부모 노드보다 작거나 가장 위에 도달하지 않을 때까지 2. 과정을 반복합니다.
# 시간복잡도 : O(log(N)) (이진트리의 최대높이만큼의 시간복잡도를 가진다.)

class MaxHeap:
    def __init__(self):
        # 이진트리를 배열로 진행하기 위해 0 번째 인덱스에 None을 넣어 인덱스 1부터 진행할 수 있도록 한다.
        self.items = [None]

    def insert(self, value):
        count = 0
        cur_index = len(self.items)
        self.items.append(value)
        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
