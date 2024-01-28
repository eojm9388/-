A, B = map(int, input().split())

common_divisor_A, common_divisor_B = A, B
divisor_num = []
num = 2 

while True:
    if common_divisor_A % num == 0 and common_divisor_B % num == 0:
        divisor_num.append(num)
        common_divisor_A //= num
        common_divisor_B //= num
        num = 2
    else:
        num += 1
    
    if common_divisor_A < num or common_divisor_B < num:
        break

num_1 = 1

for n in divisor_num:
    num_1 *= n

print(num_1)

num_A, num_B = 1, 1

while True:
    common_multiple_A , common_multiple_B = A, B
    if common_multiple_A * num_A > common_multiple_B * num_B:
        common_multiple_B *= num_B
        num_B += 1

    elif common_multiple_A * num_A < common_multiple_B * num_B:
        common_multiple_A *= num_A
        num_A += 1
    
    else:
        break

print(common_multiple_A * num_A)