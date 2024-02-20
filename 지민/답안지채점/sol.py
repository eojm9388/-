import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 정답
    answer = list(map(int, input().split()))
    # 채점표
    score_cord = [[0] * M for _ in range(N)]
    # 학생들 답안
    student = [list(map(int, input().split())) for _ in range(N)]
    # 최고점, 최저점
    min_score, max_score = 10000000, 0
    # 정답이랑 학생들의 답압을 비교하여 맞으면 1, 틀리면 0을 학생들의 채점표에 기입
    for i in range(N):
        for j in range(M):
            if student[i][j] == answer[j]:
                score_cord[i][j] = 1
            else:
                score_cord[i][j] = 0

    # 누적합 계산
    for s in range(N):
        for k in range(1, M):
            # 만약 현재 번호가 틀리지 않았다면
            # 전 번호의 점수 누적 -> 전 번호의 문제가 틀렸다면 0점은 더해도 상관없다.
            if score_cord[s][k] != 0:
                score_cord[s][k] += score_cord[s][k-1]
        # 학생의 점수
        result = sum(score_cord[s])
        # 최고점, 최저점 갱신
        if result > max_score:
            max_score = result
        if result < min_score:
            min_score = result
    # print(score_cord)
    print(f'#{tc}', max_score-min_score)