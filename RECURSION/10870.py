# 20220710 정채윤 백준 10870번

def fibo(N):
    if(N == 0):
        return 0
    elif(N == 1):
        return 1
    else:
        return fibo(N - 1) + fibo(N - 2)

if __name__=="__main__":
    N = int(input())

    print(fibo(N)) 