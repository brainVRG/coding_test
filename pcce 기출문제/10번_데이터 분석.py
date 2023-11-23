def solution(data, ext, val_ext, sort_by):
    #기준에 따른 인덱스값 저장
    case={'code':0,'date':1,'maximum':2,'remain':3}
    newData=[]
    for singleData in data:
        #기준에 맞는 데이터만 새로운 배열에 저장
        if singleData[case.get(ext)]<val_ext:
            newData.append(singleData)
    #기준에 맞는 정렬조건으로 정렬
    return sorted(newData,key=lambda x:x[case.get(sort_by)])