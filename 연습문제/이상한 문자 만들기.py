def solution(s):
    s=s.split(' ') #공백으로 나눠줌
    for i in range(len(s)): #개별 문자열 개수 만큼
        tmp=list(s[i]) #개별 문자열 리스트로 저장
        for j in range(len(s[i])):  #짝수면 대문자로, 홀수면 소문자로
            if j%2==0:
                tmp[j]=tmp[j].upper()
            else:
                tmp[j]=tmp[j].lower()
        s[i]=''.join(tmp) #리스트를 문자열로 만들어 개별 문자열에 대입
    return " ".join(s)