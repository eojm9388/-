import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    # sample 에서 찾은 passcode의 인덱스 번호
    count = 0
    # sample의 앞에서부터 순회
    for i in sample:
        # 만약 passcode의 요소와 맞다면 인덱스 증가
        if i == passcode[count]:
            count += 1
            # 만약 인덱스가 끝까지 갔다면
            # 성공
            if count == K:
                print(f'#{tc} 1')
                break
    # 반복문을 다 돌아도 break를 못 만났다면 실패
    else:
        print(f'#{tc} 0')
