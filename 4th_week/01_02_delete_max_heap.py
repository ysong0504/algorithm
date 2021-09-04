# 21-06-14
# heap 자료 구조에서 원소 삭제하기
# heap 특성 상 노드 삭제 시 맨 위에 있는 노드만 가능함
# 1. 루트 노드와 맨 끝에 있는 원소를 교체한다.
# 2. 맨 뒤에 있는 원소를 (원래 루트 노드)를 삭제한다.
# 3. 변경된 노드와 자식 노드들을 비교합니다. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 바꿉니다.
# 4. 자식 노드 둘 보다 부모 노드가 크거나 가장 바닥에 도달하지 않을 때까지 3. 과정을 반복합니다.
# 5. 2에서 제거한 원래 루트 노드를 반환합니다.
# 시간복잡도 : O(log(N)) (이진트리의 최대높이만큼의 시간복잡도를 가진다.)

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 1. 맨 위 노드와 마지막 노드 위치 변경
        cur_index = 1
        self.items[cur_index], self.items[-1] = self.items[-1], self.items[cur_index]
        deleted_node = self.items.pop()
        # del self.items[-1]

        # 바뀐 노드와 자식 노드 중 가장 큰 자식 노드와 비교해 가며 위치 변경
        # while True:
        while cur_index <= len(self.items)-1:
            left_child_index = cur_index * 2
            right_child_index = left_child_index + 1

            if right_child_index >= len(self.items):
                break

            if self.items[left_child_index] > self.items[right_child_index]:
                max_child_index = left_child_index
            else:
                max_child_index = right_child_index

            if self.items[cur_index] < self.items[max_child_index]:
                self.items[cur_index], self.items[max_child_index] = self.items[max_child_index], self.items[cur_index]
                cur_index = max_child_index

        return deleted_node

        
        



max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]

