def solution(a, b):
    daysOfMonth=[31,29,31,30,31,30,31,31,30,31,30,31] #각 달의 끝 날짜 
    days=['FRI','SAT','SUN','MON','TUE','WED','THU'] #2016년 1월 1일은 금요일이라 금요일 부터 시작
    sumDays=b-1 #1월 1일부터 지난 날짜 계산
    for i in range(a-1):
        sumDays+=daysOfMonth[i] #각 달 별 날짜 수 더해주기
    return days[sumDays%7]