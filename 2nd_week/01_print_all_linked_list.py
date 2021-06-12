#LinkedList 구현, append, 출력하기

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        # 위에 생성된 노드 클래스의 객체가 해드노드가 되었음
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            #함수 중단
            return
        #append 기능
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            # print(cur.data)
        cur.next = Node(data)

    # 탐색 노드
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


lists = LinkedList(3)
lists.append(5)
lists.print_all()
