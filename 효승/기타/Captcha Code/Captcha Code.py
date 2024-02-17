import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())

    samplecode = list(map(int, input().split()))
    passcode =  list(map(int, input().split()))

    # pop은 맨뒤에서 하는게 아니라면 시간복잡도가 O(N)임
    # 실행 시간을 줄이기 위해 역순부터 검사
    for i in range(N-1, -1, -1):
        if passcode[-1] == samplecode[i]:
            passcode.pop()

        if not passcode:
            break



    if not passcode:
        print(f'#{testcase} 1')
    else:
        print(f'#{testcase} 0')