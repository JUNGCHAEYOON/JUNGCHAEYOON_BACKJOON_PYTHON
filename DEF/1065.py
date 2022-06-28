# 20220628 정채윤 백준 1065번

def hansoo(_N):
    count = 0

    for v in range(1, _N+1):
        X = v // 100
        Y = (v % 100) // 10
        Z = v % 10

        if(X == 0):
            count += 1
        elif(Y - X == Z - Y):
            count += 1
    
    print(count)

if __name__=="__main__":
    N = int(input())

    hansoo(N)