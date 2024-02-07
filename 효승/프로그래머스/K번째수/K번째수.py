def bubbleSort(array):
    
    N = len(array)
    for i in range(0, N):
        for j in range(0, N-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
    return array

def solution(array, commands):
    answer = []
    
    for command in commands:
        temp = array[command[0]-1:command[1]]
        sorted_temp = bubbleSort(temp)
        answer.append(sorted_temp.pop(command[2]-1))
    
    return answer