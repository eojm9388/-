A, B = map(int, input().split())

common_divisor_A, common_divisor_B = A, B   # 최대공약수를 구하기 위해 변수에 두 수 할당
divisor_num = [] # 공약수를 담을 리스트
num = 2 

while True:
    # 2 부터 시작하여 두 수가 모두 나눠진다면 공약수 리스트에 추가
    if common_divisor_A % num == 0 and common_divisor_B % num == 0:
        divisor_num.append(num)
        common_divisor_A //= num
        common_divisor_B //= num
        # 다시 2부터 시작
        num = 2
    else:
        # 나눠지지 않는다면 1씩 증가
        num += 1
    
    # 께속 증가시키다가 두 수중 하나보다 커진다면 더 이상 나눌 수 없으므로 반복문 탈출
    if common_divisor_A < num or common_divisor_B < num:
        break

num_1 = 1 # 최대공약수

# 리스트를 순회하면서 공약수들을 곱하기
for n in divisor_num:
    num_1 *= n

print(num_1)

num_A, num_B = 1, 1 # 점차 커지게 하는 수

while True:

    common_multiple_A , common_multiple_B = A, B # 최소공배수를 구하기 위해 두수를 변수에 할당
    # 만약 A가 B보다 크면 B에 숫자를 곱해서 수를 높인다.
    if common_multiple_A * num_A > common_multiple_B * num_B:
        common_multiple_B *= num_B
        num_B += 1
    # 만약 B가 A보다 크면 B에 숫자를 곱해서 수를 높인다.
    elif common_multiple_A * num_A < common_multiple_B * num_B:
        common_multiple_A *= num_A
        num_A += 1
    
    # 두 수가 같아지면 반복문을 탈출한다.
    else:
        break

# 두 수중 한 수를 출력한다.
print(common_multiple_A * num_A)