def solution(n, m):
    mul=n*m  #두 수의 곱
    while m:    #유클리드 호제법 사용해 n에 최대공약수 저장
        n,m=m,n%m 
    return [n,mul/n] #최소공배수는 두수의 곱 / 최대공약수



'''
#내장 함수 사용 (lcm은 버전이 낮아 x)
from math import gcd
def solution(n, m):
    return [gcd(n,m),n*m/gcd(n,m)]

'''