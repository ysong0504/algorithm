class Dict():
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        # hash함수를 이용해서 현재 딕셔너리의 최대길이를 기준으로 연산을 해준다.
        index = hash(key) % len(self.items)
        self.items[index] = value
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put('test', 3)
print(my_dict.get('test'))
