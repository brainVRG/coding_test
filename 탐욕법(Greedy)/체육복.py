def solution(n, lost, reserve):
    lost.sort() #정렬을 하지 않아 테스트 통과하지 못함, 정렬 추가
    reserve.sort()
    for l in lost[:]:   #효율적으로 제거
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    answer=n-len(lost)
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]==reserve[j]+1:
                answer+=1
                reserve[j]=-3
                break
            if lost[i]==reserve[j]-1:
                answer+=1
                reserve[j]=-3
                break
    return answer