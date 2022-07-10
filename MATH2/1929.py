# 20220710 정채윤 백준 1929번 

def isSo(X):
    if X == 1:
        return False
    for I in range(2, int(X ** 0.5) + 1):
        # 소수 검사는 2부터 X 의 1/2 승 까지만 하면 됨
        if(X % I == 0):
            return False
    return True

if __name__=="__main__":
    M, N = map(int,input().split())

    for I in range(M, N + 1):
        if(isSo(I)):
            print(I)