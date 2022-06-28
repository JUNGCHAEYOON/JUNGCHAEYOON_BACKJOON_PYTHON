# 20220628 정채윤 백준 2675번

if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        X = list(map(str,input().split()))
        R = int(X[0])
        S = X[1]

        for I in S:
            for _ in range(R):
                print(I, end = "")
        print()
