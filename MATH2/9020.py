# 20220710 정채윤 백준 9020번 

def isPrime(X):
    if(X == 1):
        return False
    for I in range(2, int(X ** 0.5) + 1):
        if(X % I == 0):
            return False
    return True

if __name__=="__main__":
    for _ in range(int(input())):
        N = int(input())

        A, B = N // 2, N // 2
        while 1:
            if(isPrime(A) and isPrime(B)):
                print("%d %d" %(A, B))
                break
            else:
                A -= 1
                B += 1

        