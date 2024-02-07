import sys
sys.stdin = open('a4.Ladder1.txt')


for _ in range(10):
    t = int(input())
    N = 100
    MAP = [list(map(int,input().split())) for _ in range(N)]

    #도착 지점을 찾는다
    row = 0

    for goal in range(N):
        if MAP[N-1][goal] == 2:
            row = goal
            break

    col = 99

    while True:

        if col == 0:
            break

        #오른쪽을 우선순위
        if row < N - 1 and MAP[col][row+1]:
            while row < N - 1 and MAP[col][row + 1]:
                row = row + 1
            else:
                col = col - 1

        elif row > 0 and MAP[col][row-1]:
            while row > 0 and MAP[col][row - 1]:
                row = row - 1
            else:
                col = col - 1

        else:
            col = col - 1


    print(f'#{t} {row}')