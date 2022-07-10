# 20220710 정채윤 백준 2581번 

def isSo(X):
    if(X == 1):
        return False
    for I in range(2, X):
        if(X % I == 0):
            return False
    return True

if __name__=="__main__":
    M = int(input())
    N = int(input())

    total = 0
    min = N
    for I in range(M, N + 1):
        if(isSo(I)):
            total += I
            if(I < min):
                min = I

    if(total != 0):
        print(total)
        print(min)
    else:
        print(-1)
