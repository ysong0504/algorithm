# 작성일 : 2021-06-17
# 문제설명 : 아래 기준에 맞춰 장르별로 가장 많이 재생된 노래를 두개 씩 취합하려고한다.
# 1. 장르별 재생된 노래 회수를 합쳤을 때 그 중 가장 큰 장르를 구한다.
# 2. 1에서 구한 장르내에서 재생 횟수가 가장 많은 노래를 순차적으로 구한다. (최대 2개)
# 3. 만약 재생된 횟수가 동일할 시 고유 번호(인덱스)가 낮은 노래를 먼저 찾는다.

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 인덱스별 연결되는 linkedlist (tuple은 뭐지)
class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append(key, value)

    def put(self, key):

        for k, v in self.items:
            if key == k:
                return v



def get_melon_best_album(genre_array, play_array):
    album_dict = {}

    # 구현해보세요!
    return []


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!