# 20220704 정채윤 백준 2292번

if __name__=="__main__":
    X = int(input())

    if(X == 1):
        print(1)
    else:
        N = 1
        t = 1
        while (True) :
            if(N < X and X <= N + 6 * t):
                print(t + 1)
                break
            else:
                N = N + 6 * t
                t += 1


    