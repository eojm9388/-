import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    height, width = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if arr[i][j] == 2:
                start_x, start_y = i, j

    dx = [1, -1]
    dy = [1, -1]

    limit = 0
    stack = []
    flag = True

    while flag:

        limit += 1
        stack.append([start_x, start_y])
        visited = [[False] * width for _ in range(height)]

        while stack:
            now_x, now_y = stack.pop()

            if arr[now_x][now_y] == 3:
                flag = False
                break

            for i in range(2):
                for j in range(1, limit+1):
                    move_x = now_x + j * dx[i]

                    if 0 <= move_x < height and not visited[move_x][now_y]:
                        if arr[move_x][now_y] >= 1:
                            stack.append([move_x, now_y])
                            visited[move_x][now_y] = True
            
            
            for i in range(2):
                for j in range(1, width+1):
                    move_y = now_y + dy[i] * j

                    if move_y < 0 or move_y >= width or arr[now_x][move_y] == 0 or visited[now_x][move_y] == True:
                        break
                    else:
                        stack.append([now_x, move_y])
                        visited[now_x][move_y] = True

    print(f'#{testcase} {limit}')