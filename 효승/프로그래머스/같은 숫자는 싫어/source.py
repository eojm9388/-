def solution(arr):
    answer = [arr[0]]
    top = 0
    for i in arr:
        if answer[top] != i:
            answer.append(i)
            top += 1
    
    return answer