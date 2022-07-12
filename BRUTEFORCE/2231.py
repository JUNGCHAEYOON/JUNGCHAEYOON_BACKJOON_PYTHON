# 20220712 정채윤 백준 2231번

def sang(N):
    A = list(str(N))
    B = N - 9 * len(A)
    if(B <= 0):
        B = 1

    for I in range(B, N + 1):
        arr = list(map(int,str(I)))
        total =  I + sum(arr)
        if(total == N):
            return I
        
    return 0
    
if __name__=="__main__":
    N = int(input())

    print(sang(N))