def solution(participant, completion): 
    participant.sort()
    completion.sort()
    for i in range(len(completion)): #리스트를 하나씩 돌며 찾으면 시간초과, 정렬 후 다른 값일때 리턴하게 변경
        if participant[i]!=completion[i]:
            return participant[i]
    return participant[-1]