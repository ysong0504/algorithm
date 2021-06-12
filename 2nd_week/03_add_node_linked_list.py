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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        count = 0

        while count < index:
            cur = cur.next
            count += 1
        return cur

    def add_node(self, index, data):
        #신규 노드 생성
        new_node = Node(data)
        # 해당 인덱스의 기존 값 임시 저장텐데 s
        origin_node = self.get_node(index)   #궁금한거..  self.get_node(0) 과 self.head의 차이가 있을까?

        if index == 0:
            # 인덱스가 0 일경우 노드헤드에 저장
            self.head = new_node
            return

        # 해당 인덱스의 앞 노드 구하기
        prev_node = self.get_node(index - 1)
        #앞서 구한 prev_node옆에 next 이용해서 신규 노드 저장
        prev_node.next = new_node
        #신규 노드 옆에 기존에 있던 노드 저장
        new_node.next = origin_node


#
linked_list = LinkedList(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
# linked_list.print_all()
linked_list.add_node(0, 4)
linked_list.print_all()
# linked_list.get_node(3).data # -> 5를 들고 있는 노드를 반환해야 합니다!
