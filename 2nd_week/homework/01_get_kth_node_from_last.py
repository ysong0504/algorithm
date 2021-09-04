#Q. 링크드 리스트의 '끝에서' K번째 값을 반환하시오.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        count = 1
        cur = self.head

        #0번째일 시 노드헤드 반환
        if k == 0:
            return cur

        #count가 k와 동일한 값이 될 때까지 node를 이동시킨 후
        #해당 노드 값을 반환한다.
        while count != k:
            cur = cur.next
            count += 1

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last().data)  # 7이 나와야 합니다!