class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # 신규 노드 생성
        new_head = Node(value)
        # 신규 노드 옆에 기존 헤드 추가
        new_head.next = self.head
        # 헤드에 신규 노드 할당
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "스택이 비어있습니다."
        deleted_value = self.head
        self.head = self.head.next
        return deleted_value

    def peek(self):
        if self.is_empty():
            return "스택이 비어있습니다."
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # None일 시 True값 반환
        return self.head is None
        # if self.head is None:
        #     return True
        # else:
        #     return False


# 테스트
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.is_empty())
print(stack.pop().data)
print(stack.pop().data)
print(stack.is_empty())

