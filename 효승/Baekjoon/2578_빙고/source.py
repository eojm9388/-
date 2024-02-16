def bingoCheck(check):
    # 빙고의 개수를 리턴하는 함수    
    bingo = 0

    # 가로 빙고의 개수를 검사
    for i in range(5):
        if sum(check[i]) == 5:
            bingo += 1

    # 세로 빙고의 개수를 검사
    for i in range(5):
        temp = 0
        for j in range(5):
            temp += check[j][i]
        if temp == 5:
            bingo += 1
    temp = 0
    temp2 = 0

    # 대각선 빙고의 개수를 검사
    for i in range(5):
        temp += check[i][i]
        temp2 += check[i][4-i]
    if temp == 5:
        bingo += 1
    if temp2 == 5:
        bingo += 1

    return bingo

# 빙고 판을 입력
board = [list(map(int, input().split())) for _ in range(5)]

# 빙고 숫자를 입력
bingo = [list(map(int, input().split())) for _ in range(5)]

bingo_list = []

# 계산하기 편하게 리스트에 빙고 번호를 다시 할당
for i in range(5):
    for j in range(5):
        bingo_list.append(bingo[i][j])


# 어떤 숫자가 나왔는지 체크하기 위한 2차원 리스트 만듦
# 1이면 나온 숫자
check = [[0] * 5 for _ in range(5)]

count = 0

# 빙고 번호를 순회
for i in range(25):
    count += 1
    number = bingo_list[i]

    # 입력받은 숫자 위치에 있는 check를 1로 바꿔줌
    for j in range(5):
        if number in board[j]:
            check[j][board[j].index(number)] = 1
            break
    
    # 빙고 체크를 함. 3이상이라면 반복 종료
    if bingoCheck(check) >= 3:
        break
        
print(count)