def solution(strings, n):
    return sorted(strings,key=lambda x:(x[n],x)) #n번째 인덱스를 우선해서 정렬 후 기존방식으로 정렬