# 작성일 : 21-06-16
# 링크드 리스트를 이용한 큐 구현하기
# 큐란, First In First Out, 먼저 들어간 값은 제일 마지막에 출력되는 특징
# 보통 순서대로 무언가를 처리할 때 또는 먼저해야하는 일들을 저장하고 싶을 때 사용

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        # 큐 특성상 존재하는 마지막 노드
        self.tail = None

    # 맨 뒤에 데이터 추가
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        # 1차적으로 신규 노드를 테일.next에 놓고
        self.tail.next = new_node
        # 최종적으로 신규 노드를 테일로 전환한다.
        self.tail = new_node
        return

    # 맨 앞에 데이터 뽑기
    def dequeue(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "the queue is empty"
        deleted_value = self.head
        self.head = self.head.next
        return deleted_value.data

    # 맨 앞 데이터 보기
    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "the queue is empty"
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None

queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.dequeue())
print(queue.peek())