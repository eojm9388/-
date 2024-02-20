w, h = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

# 오른쪽으로 개미가 붙는데까지 걸리는 시간
right_t = w - p
# 위로 개미가 붙는데까지 걸리는 시간
top_t = h - q

# 가로로 움직이는 시간과 세로로 움직이는 시간을
# 따로 봄
# 오른쪽에 개미가 붙었을 때 남은 시간
w_t = t - right_t
# 위에 개미가 붙었을 때 남은 시간
h_t = t - top_t

# 이 값이 짝수라면 개미는 오른쪽에서 출발
# 홀수라면 개미는 왼쪽에서 출발
# (w_t % w) : 더 이상 벽에 튕기지 않고 가는 남은 거리
if (w_t // w) % 2 == 0:
    # 오른쪽에서 왼쪽으로 이동
    x = w - (w_t % w)

else:
    # 왼쪽에서 오른쪽으로 이동
    x = 0 + (w_t % w)
# 이 값이 짝수라면 개미는 위에서 출발
# 홀수라면 개미는 아래에서 출발
# (w_t % w) : 더 이상 벽에 튕기지 않고 가는 남은 거리
if (h_t // h) % 2 == 0:
    # 위에서 내려온다
    y = h - (h_t % h)

else:
    # 아래에서 올라간다
    y = 0 + (h_t % h)

print(x, y)

