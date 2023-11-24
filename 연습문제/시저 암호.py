def solution(s, n):
    s=list(s)
    for i in range(len(s)):
        if 97<=ord(s[i])<=122:
            s[i]=chr((ord(s[i])%97+n)%26+97)
        elif 65<=ord(s[i])<=90:
            s[i]=chr((ord(s[i])%65+n)%26+65)
    #print(ord(' '),ord('a'),ord('z'),ord('A'),ord('Z'))
    return ''.join(s)