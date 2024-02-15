# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())//10
    memo = [0] * (N+1)
    memo[1] = 1
    memo[2] = 3
    
    # 점화식
    for i in range(3, N+1):
        memo[i] = memo[i-1] + 2*memo[i-2]

    print(f'#{tc}', memo[N])