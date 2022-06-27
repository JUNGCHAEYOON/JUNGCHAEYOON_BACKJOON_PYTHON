# 20220627 정채윤 백준 2525번

def oven(_H, _M, _T):
    sumM = _M + _T
    sumH = _H + (sumM // 60)

    if(sumH >= 24):
        print(sumH % 24, sumM % 60)
    else:    
        print(sumH, sumM % 60)

if __name__ == "__main__":
    H, M = map(int, input().split())
    T = int(input())

    oven(H, M, T)