# 20220710 정채윤 백준 10872번

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N - 1)

if __name__=="__main__":
    N = int(input()) 
    
    print(factorial(N))