# 21-06-14
# heap 자료 구조에서 원소 삭제하기

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 1. 루트 노드와 마지막 노드의 위치를 바꿔준다.
        self.items[1], self.items[-1] = self.items[-1], self.items[1]

        # 2. 마지막 노드는 삭제하며 해당 값은 반환하기 위해 변수에 할당한다.
        prev_root = self.items.pop()

        # 3. 루트 노드로 이동한 값은 자식 노드들과 비교하며 heapify 해준다.
        cur_idx = 1

        # 3_1. 현재 노드가 마지막 인덱스에 도달하기 전까지 반복
        while cur_idx <= len(self.items) - 1:
            left_idx = cur_idx * 2
            right_idx = cur_idx * 2 + 1
            compare_idx = cur_idx

            if right_idx > len(self.items) or left_idx > len(self.items):
                break
            # 3_2 왼쪽, 오른쪽 자식 중 더 큰 값 구하기
            if self.items[left_idx] > self.items[right_idx]:
                compare_idx = left_idx
            else:
                compare_idx = right_idx

            # 3_3 만약 자식 노드가 크다면 자리 변경
            if self.items[compare_idx] > self.items[cur_idx]:
                self.items[compare_idx], self.items[cur_idx] = self.items[cur_idx], self.items[compare_idx]
                cur_idx = compare_idx

            # # 만약 비교 자식 노드와
            # if compare_idx == cur_idx:
            #     break

        return prev_root


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
# max_heap.delete()
