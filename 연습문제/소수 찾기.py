from math import sqrt
def solution(n):
    primeNumArray=[False,False]+[True]*(n-1) #0부터 n까지 소수 여부 저장된 배열
    for i in range(2,int(sqrt(n))+1): #n의 소수 판별위해선 n의 제곱근 까지만 확인하면 됨
        if primeNumArray[i]: #에라스토테네스의 체 활용
            for j in range(i*i,n+1,i):
                primeNumArray[j]=False
    return primeNumArray.count(True)