import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    hw = list(map(int, input().split()))
    print(f'#{tc}', end = ' ')
    for i in range(1, N+1):
        if i not in hw:
            print(i, end = ' ')
    print()