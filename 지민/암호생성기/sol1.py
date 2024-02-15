# import sys
# sys.stdin = open('input.txt')

from collections import deque

# 한 사이클
def cycle():
    # 1부터 5까지 암호의 맨 앞 숫자에 빼준다
    for i in range(1, 6):
        # 암호의 맨 앞 숫자
        num = q.popleft()
        # print(num)
        num -= i
        # 만약 숫자가 0이하라면 맨 뒤로 보내고 종료
        if num <= 0:
            num = 0
            q.append(num)
            return True
        # 뺀 숫자를 맨 뒤로 보내기
        else:
            q.append(num)
    # print(q)

for t in range(1, 11):
    # 테스트 케이스 입력
    tc = int(input())
    # 처음 암호
    number = list(map(int, input().split()))
    # 큐에 할당
    q = deque(number)
    # 조건문을 확인할 때 1사이클이 돌아간다.
    while True:
        # 만약 0이하의 숫자가 맨 뒤에 보내졌다면
        # 반복문 탈출
        if cycle():
            break
    # 테스트 케이스 출력
    print(f'#{tc}', end=' ')
    # 결과값 출력
    for j in q:
        print(j, end=' ')

    print()
