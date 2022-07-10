# 20220710 정채윤 백준 4948번

def isPrime(X):
    if X == 1:
        return False
    for I in range(2, int(X ** 0.5) + 1):
        if(X % I == 0):
            return False
    return True  

if __name__=="__main__":
    
    # 문제에서 주어진 숫자범위만 소수만 뽑아 리스트로 만듬
    ARR = list(range(2, 246912))
    primer = []
    for I in ARR:
        if(isPrime(I)):
            primer.append(I)

    while 1:
        N = int(input())
        if(N == 0): break

        cnt = 0
        # 소수 리스트에서 N 초과 2N 이하인 값만 계산
        for I in primer:
            if(N < I <= 2 * N):
                cnt += 1
        print(cnt)

