def solution(nums):
    lenOfNums=len(nums)
    #중복된 포켓몬은 1마리로 계산하기 때문에 set으로 중복 제거
    setNums=set(nums)
    pickNum=lenOfNums/2
    #중복 제거된 포켓몬들이 고를 수 있는 숫자 보다 많을 시 가져갈 수 있는 포켓몬의 수 반환
    if len(setNums)>=pickNum:
        return pickNum
    #중복 제거된 포켓몬들이 고를 수 있는 숫자 보다 적을 시 중복 제거된 포켓몬들의 수 반환
    elif len(setNums)<pickNum:
        return len(setNums)