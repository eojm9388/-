import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    
    correct_answer = list(map(int, input().split()))
    student_answer = [list(map(int, input().split())) for _ in range(N)]

    # 각 학생들의 점수 총합을 저장할 리스트
    score_sum = [0] * N
    
    # 각 학생에 문제 전체에 대해서 순회
    for i in range(N):
        # 각 학생의 문제마다의 점수
        score = 0

        # 문제를 순회함
        for j in range(M):
            # 정답이라면, 이전 점수 + 1
            if student_answer[i][j] == correct_answer[j]:
                score += 1
            # 아니라면 연속된 점수를 0으로 초기화
            else:
                score = 0
            # 한 문제를 풀 때마다 총점에 더함
            score_sum[i] += score

    print(f'#{testcase} {max(score_sum) - min(score_sum)}')