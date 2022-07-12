# 20220712 정채윤 백준 2798번

if __name__=="__main__":
    N, M = map(int,input().split())
    L = list(map(int,input().split()))

    total = 0

    for I in L:
        for J in L:
            for K in L:
                if(I != J and J != K and I != K and I + J + K <= M and total < I + J + K):
                    total = I + J + K

    
    print(total)