N = int(input()) # 과목의 개수

score_list = list(map(int, input().split())) # 각 과목의 원래 점수
max_score = max(score_list) # 시험 최고점

# 원래점수 / 최고점수 * 100 = 새로운 점수
# 반복문으로 새로운 점수 리스트 컴프리헨션 생성
new_score_list = [(score/max_score)*100 for score in score_list]

# 평균 계산
print(sum(new_score_list)/N)