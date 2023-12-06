def solution(n, arr1, arr2):
    answer = [''for i in range(n)] #정답배열
    for i in range(n):
        for j in bin(arr1[i]|arr2[i])[2:].zfill(n): # 비트 or 연산으로 벽 찾기, 이진수 자리 맞추기 위해 zfill사용
            if j=='0':
                answer[i]+=' '
            else:
                answer[i]+='#'
    return answer