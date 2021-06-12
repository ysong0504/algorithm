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


def get_linked_list_sum(linked_list_1, linked_list_2):
    num_1 = _get_linked_list_sum(linked_list_1)
    num_2 = _get_linked_list_sum(linked_list_2)

    # 구현해보세요!
    return num_1 + num_2


# 중복되는 코드는 하나의 함수로 묶는다.
def _get_linked_list_sum(linked_list):
    num = 0
    cur = linked_list.head
    while cur is not None:
        num = num * 10 + cur.data
        cur = cur.next
    return num


# def get_linked_list_sum(linked_list_1, linked_list_2):
#     # str 버전..
#     cur_1 = linked_list_1.head
#     cur_2 = linked_list_2.head
#     num_1 = ""
#     num_2 = ""
#     while cur_1 is not None:
#         num_1 += str(cur_1.data)
#         cur_1 = cur_1.next
#
#     while cur_2 is not None:
#         num_2 += str(cur_2.data)
#         cur_2 = cur_2.next
#
#     # 구현해보세요!
#     return int(num_1) + int(num_2)


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))