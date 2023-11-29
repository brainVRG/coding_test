def solution(arr):
    if len(arr)==1: #제한조건 1. arr은 길이 1 이상인 배열입니다. 2. 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다. 을 통해 같은 숫자는 중복 저장되지 않음으로 길이가 1이면 [-1] 반환
        return [-1]
    arr.remove(min(arr)) #최솟값 제거
    return arr



'''
#시간초과 오류 나온 코드
def solution(arr):
    return [e for e in arr if e!=min(arr)] or [-1]
'''