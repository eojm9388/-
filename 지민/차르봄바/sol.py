import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 마을의 크기 N, 차르봄바의 파워 P
    N, P = map(int, input().split())
    # 마을을 나타내는 2차원 리스트
    village = [list(map(int, input().split())) for _ in range(N)]
    # 결과값들을 모을 리스트
    result_list = []
    # 마을 전체 요소를 순회
    for i in range(N):
        for j in range(N):
            # 폭탄을 떨어뜨릴 위치의 바이러스 수: 초기값
            result = village[i][j]
            # 폭탄이 떨어진 위치에서 P 크기만큼 상하좌우로 퍼져나가면서 제거한 바이러스 수
            # 상하좌우
            for k in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                # P 크기만큼 증가
                for p in range(1, P+1):
                    ni = i + k[0] * p
                    nj = j + k[1] * p
                    # 제한범위 내에서만 더한다
                    if 0<=ni<N and 0<=nj<N:
                        result += village[ni][nj]
            # 결과값 리스트에 추가
            result_list.append(result)
    # 최대값 출력
    print(max(result_list))

