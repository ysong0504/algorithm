class Node:
    def __init__(self, key, value):
        # 노트 클라스 생성 (일반 링크드리스트 노드와 유사하지만 data대신 key, value값을 받는다.)
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 참조값
        self.prev = None  # 이전 노드에 대한 참조값


class LinkedList:
    # 생성자
    def __init__(self):
        self.head = None  # 링크드 리스트 가장 앞 노드
        self.tail = None  # 링크드 리스트 가장 뒤 노드

    # key를 이용하여 특정 노드 탐색 메소드
    def find_node_with_key(self, key):
        # 시작은 맨 앞 노드부터
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur
            # 마지막 cur 까지 이동
            cur = cur.next

    # 추가/삽입 메소드
    def append(self, key, value):
        # key, value가 포함된 노드 생성
        new_node = Node(key, value)

        if self.head is None:
            # 만약 링크드리스트가 비어있다면,
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node   # 마지막 노드 뒤에 신규 노드 추가
            new_node.prev = self.tail   # 신규 노드 뒤에는 기존에 있던 마지막 노드 추가
            self.tail = new_node        # self.tail 업데이트

    # 삭제 메소드
    def delete(self, node_to_delete):
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None

        elif node_to_delete is self.head:
        # 가장 앞 노드 삭제 시
            self.head = self.head.next
            self.head = None

        elif node_to_delete is self.tail:
        # 가장 뒤 노드 삭제 시
            self.tail = self.tail.prev
            self.tail = None

        else:
        # 두 노드 사이에 데이터 삭제 시
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    # 링크드 리스트를 문자열로 출력해주는 메소드
    def print_all(self):
        res_str = ""

        cur = self.head
        while cur is not None:
            # res_str에 노드 데이터를 key: value 형식으로 할당한다.
            res_str += "{}: {}\n".format(cur.key, cur.value)
            cur = cur.next

        return res_str


linked_list = LinkedList(0)
# LinkedList.append(101, '최지웅')
linked_list.append(204, '강영훈')
linked_list.append(305, '성태호')

print(LinkedList.print_all)