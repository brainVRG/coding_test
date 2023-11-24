def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1): #제곱근까지만 확인
        if n%i==0:
            answer+=i
            if i!=n//i: # 2*2=4 같은경우에는 중복해서 더하지 않음
                answer+=n//i
    return answer