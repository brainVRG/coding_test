def solution(answers):
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    answer=[0,0,0]
    for i,ans in enumerate(answers):
        if ans==a[i%len(a)]:
            answer[0]+=1
        if ans==b[i%len(b)]:
            answer[1]+=1
        if ans==c[i%len(c)]:
            answer[2]+=1
    maxN=max(answer)
    result=[]
    for i,amount in enumerate(answer):
        if amount==maxN:
            result.append(i+1)
    return result