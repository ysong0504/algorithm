# 작성일 : 21-06-16
# 주제 : 스택
# 난이도 : 하

# 문제명 : 스택
# 문제설명 :
# 백준 코드번호 : 10828

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, value):
        new_node = Node(value)
        self.count += 1
        if self.is_empty() == '1':
            self.head = new_node
        else:
            self.head.next = self.head
            self.head = new_node
        return new_node.data

    def pop(self):
        if self.is_empty() == '1':
            return '-1'
        else:
            deleted_value = self.head
            self.head = self.head.next
            self.count -= 1
            return deleted_value.data

    def size(self):
        return self.count

    def is_empty(self):
        if self.head is None:
            return '1'
        else:
            return '0'

    def top(self):
        if self.is_empty() == '1':
            return '-1'
        else:
            return self.head.data


lists = input()
lists = int(lists)
stack = Stack()
for i in range(lists):
    # input_value = sys.stdin.readline().split()
    input_value = input().split()
    if input_value[0] == 'push':
        print(stack.push(input_value[1]))
    elif input_value[0] == "empty":
        print(stack.is_empty())
    elif input_value[0] == "pop":
        print(stack.pop())
    elif input_value[0] == "size":
        print(stack.size())
    elif input_value[0] == "top":
        print(stack.top())

