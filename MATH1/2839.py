# 20220709 정채윤 백준 2839번 실버4

def seoltang(N):
    if(N == 1 or N == 2 or N == 4 or N == 7):
        return -1
    X = N % 5
    Y = N // 5
    if(X == 0):
        return Y
    elif(X == 1 or X == 3):
        return Y + 1
    else:
        return Y + 2

if __name__=="__main__":
    N = int(input())

    print(seoltang(N))
    
    
