def solution(x):
    return True if x%sum(int(i) for i in f'{x}')==0 else False