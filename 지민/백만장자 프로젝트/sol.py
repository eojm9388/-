# import sys
# sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 각 날의 매매가
    sales = list(map(int, input().split()))
    # 최대 이익
    result = 0
    # 최대 가격
    # 초기 최대 가격은 맨 마지막부터
    max_price = sales[-1]
    # 뒤에서부터 진행
    for i in range(N-1, -1, -1):
        # 최대 가격보다 매매가가 작다면 구매해서 판다
        if sales[i] <= max_price:
            result += max_price - sales[i]
        # 최대 가격보다 매매가가 높다면 최대 가격 갱신
        else:
            max_price = sales[i]


    print(f'#{tc}',result)