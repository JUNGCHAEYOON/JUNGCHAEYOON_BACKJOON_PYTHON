# 20220627 정채윤 백준 10871번

if __name__=="__main__":
    N, X = map(int,input().split())
    A = list(map(int, input().split()))

    for i in range(N):
        if(A[i] < X):
            print(A[i], end = " ")