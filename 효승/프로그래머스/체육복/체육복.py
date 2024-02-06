def solution(n, lost, reserve):
    answer = 0
    
    # 중복을 제거하기 위해 set를 선언하고, 차집합을 사용함
    # 이를 통해 체육복이 여분이 있고 잃어버린 사람을 처리 가능
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)


    # 여유분이 있는 학생을 순회하며 앞뒤번호라면 빌려줌
    for i in reserve_set:
        
        if i-1 in lost_set:
            lost_set -= {i-1}
            
        elif i+1 in lost_set:
            lost_set -= {i+1}

    answer = n - len(lost_set)
    return answer