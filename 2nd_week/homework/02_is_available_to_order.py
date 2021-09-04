# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.

# binary search를 이용해서 찾아보장
def is_available_to_order(menus, orders):
    # 오름차순으로 정렬
    shop_menus.sort()
    shop_orders.sort()
    is_exist = True

    # 주문한 메뉴 수 만큼 for문 진행
    for order in shop_orders:
        if not is_exist:
            return False
        is_exist = ""
        start_index = 0
        end_index = len(shop_menus) - 1
        # while문을 통해 메뉴와 주문내역 비교
        while start_index <= end_index:
            mid_index = (start_index + end_index) // 2
            menu = shop_menus[mid_index]
            if order == menu:
                is_exist = True
                break
            elif order < menu:
                # 왼쪽 탐색
                end_index = mid_index - 1
            elif order > menu:
                # 오른쪽 탐색
                start_index = mid_index + 1

    return True


shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
# shop_menus = ["만두", "떡볶이", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

result = is_available_to_order(shop_menus, shop_orders)
print(result)
