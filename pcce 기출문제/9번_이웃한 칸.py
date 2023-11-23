def solution(board, h, w):
    #인덱스가 넘어가는 현상 방지하기 위해 위아래로 2칸씩 더 큰 배열 만듬
    bigBoard=[[0 for col in range(len(board[0])+2) ] for row in range(len(board)+2)]
    #만든 배열에 값들 집어넣기
    for row in range(1,len(bigBoard)-1):
        for col in range(1,len(bigBoard)-1):
            bigBoard[row][col]=board[row-1][col-1]
    answer=0
    h+=1
    w+=1
    if bigBoard[h][w-1]==bigBoard[h][w]:
        answer+=1
    if bigBoard[h-1][w]==bigBoard[h][w]:
        answer+=1
    if bigBoard[h][w+1]==bigBoard[h][w]:
        answer+=1
    if bigBoard[h+1][w]==bigBoard[h][w]:
        answer+=1
    print(bigBoard)
    return answer