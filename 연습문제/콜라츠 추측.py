def solution(num,time=0):
    if num==1:
        return 0
    if time==501:
        return -1
    num= num//2 if num%2==0 else num*3+1
    time+=1
    if num==1:
        return time
    return solution(num,time)