def solution(sizes):
    answer = 0
    
    # 초기값 설정
    # max_1이 더 긴 변의 길이, max_2가 작은 변의 길이
    max_1 = 1
    max_2 = 0
    
    for size in sizes:
        
        # 입력받은 사각형의 변의 길이중 큰 변의 길이가 기존의 max보다 크다면
        # max_1 갱신
        if max(max_1, max_2) < max(size):
            max_1 = max(size)

        # 입력받은 사각형에서 작은 변의 길이가 기존의 max보다 크다면
        # max_2 갱신
        if min(max_1, max_2) < min(size):
            max_2 = min(size)
    
    answer = max_1 * max_2
    
    
    return answer