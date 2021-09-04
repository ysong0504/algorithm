class Node:
    # 지하철 역 노드를 나타내는 클래스
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits


# 노드 인스턴스 생성
# 연결 관계를 나타내는 그래프에서는 모든 노드가 동등한 위치에 있다.
station_0 = Node('신림역', 3)
station_1 = Node('화곡역', 7)

# 노드들을 리스트에 저정 -> 인덱스로 접근하기 때문에 O(1)
# stations = [station_0, station_1]

# 노드들을 해시 테이블에 저정 -> key로 가져오기때문에 O(1)
stations = {
    '신림역': station_0,
    '화곡역': station_1
}