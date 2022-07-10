# 20220710 정채윤 백준 1978번 

if __name__=="__main__":
    X = int(input())
    
    arr = list(map(int,input().split()))

    cnt = 0
    isSo = True
    for X in arr:
        if(X == 1):
            isSo = False
        for I in range(2, X):
            if(X % I == 0):
                isSo = False
                break
        if(isSo):
            cnt += 1
        else:
            isSo = True
    
    print(cnt)