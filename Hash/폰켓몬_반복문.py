def solution(nums):
    lenOfNums=len(nums)
    answer=[]
    #저장된 포켓몬 리스트 확인해서 다른 종류만 배열에 저장
    for j in nums:
        if j not in answer:
            answer.append(j)
    return min(lenOfNums//2,len(answer))
            

