def solution(arr):
    answer = []
    lastNum=-1
    for i in arr:
        if i!=lastNum:
            answer.append(i)
            lastNum=i
    return answer