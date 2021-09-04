top_heights = [6, 9, 5, 7, 4]
#url : https://www.notion.so/3-83a14432311c401598ce3c05e3be25c4
# range(시작점, 종료지점, step)

# 0으로 초기화된 배열 생성
def get_receiver_top_orders(heights): #O(N^2)
    n = len(heights)
    order_arr = [0] * n

    while heights: #O(N)
        # 맨 마지막 값을 받는다.
        height = heights.pop()
        for idx in range(len(heights) - 1, 0, -1):  #O(N)
            if heights[idx] > height:
                order_arr[len(heights)] = idx + 1
                break

    return order_arr




print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!