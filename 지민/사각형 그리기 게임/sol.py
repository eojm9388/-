# import sys
# sys.stdin = open("input.txt")

T = int(input())
# 사각형을 구해주는 함수
def square(i, j):
    # 만든 사각형의 면적들을 넣어둘 리스트
    area = []
    # print('i, j:', i, j)
    # 우측 하단의 좌표값을 구한다.
    # ex) N = 3
    # i, j = (0, 1) -> x, y = (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)
    for x in range(i, N):
        for y in range(j, N):
            # 만약 우측 하단의 좌표와 현재 좌표값이 같다면
            if board[x][y] == board[i][j]:
                # 면적 추가, 면적 = 세로 * 가로
                area.append((x-i+1)*(y-j+1))

            # print('x, y:', x, y)
    # print(area)
    # 면적 리스트 반환
    return area

for tc in range(1, T+1):
    # 게임판의 크기
    N = int(input())
    # 만들 수 있는 면적들
    result = []
    # 게임판 2차원 리스트
    board = [list(map(int, input().split())) for _ in range(N)]
    # 게임판의 모든 좌표를 순회하면 만들 수 있는 사각형의 면적을 구한다.
    for i in range(N):
        for j in range(N):
            result += square(i, j)
    # print(result)
    # 최대 면적
    max_area = max(result)
    # 최대 면적 개수 출력
    print(f'#{tc}', result.count(max_area))