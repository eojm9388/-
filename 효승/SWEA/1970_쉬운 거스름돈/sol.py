import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    
    # 돈의 단위를 미리 리스트로 정리해둠
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    # 각 돈이 몇개 필요한지 세는 리스트를 만듦
    count = [0] * len(money_list)

    # 입력받은 액수
    money = int(input())

    # 각 돈의 단위를 순회하며
    for i in range(len(money_list)):

        # 최대 몇 개가 필요한지 구함
        count[i] = money // money_list[i]

        # 나머지를 구함
        money %= money_list[i]

        # 순회하면서 점점 작은 단위로 이동할것

    print(f'#{testcase}')
    print(f'{" ".join(map(str, count))}')