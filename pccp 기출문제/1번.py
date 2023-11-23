def solution(bandage, health, attacks):
    maxHealth=health
    rowSuccess=0
    attackStatus=False
    for i in range(1,attacks[-1][0]+1):#attack의 최대 공격시간에 맞춰 range설정
        for attack in attacks:#시간에 맞을때만
            if attack[0]==i:
                health-=attack[1]#체력 - 공격
                attackStatus=True
                rowSuccess=0#연속 성공 초기화
                break
        if health<=0:#0 이하 -1 반환
            return -1
        if not attackStatus:#공격 받지 않았을 때만
            health+=bandage[1]#초당 회복량 회복
            rowSuccess+=1
            if rowSuccess==bandage[0]:#연속 성공 했을때
                health+=bandage[2]#추가 회복량 회복
                rowSuccess=0#연속 성공 초기화
        health=min(maxHealth,health)#최대 체력 넘을 수 없음으로 검사
        attackStatus=False
    return health