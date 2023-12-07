def solution(dartResult):
    sumArr=[]
    num='' 
    for i in dartResult:
        if i.isdigit():
            num+=i#10처리 하기 위해 문자열에 더해주기
        elif i=='S':
            sumArr.append(int(num))
            num=''#숫자 초기화
        elif i=='D':
            sumArr.append(int(num)**2)
            num=''
        elif i=='T':
            sumArr.append(int(num)**3)
            num=''
        elif i=='#':
            sumArr[-1]=-sumArr[-1]
        elif i=='*':
            if len(sumArr)==1:#첫번째 스타상 예외 처ㅓ리
                sumArr[-1]=2*sumArr[-1]
            else:
                sumArr[-1]=2*sumArr[-1]
                sumArr[-2]=2*sumArr[-2]
    return sum(sumArr)