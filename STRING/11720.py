# 20220628 정채윤 백준 11720번

if __name__=="__main__":
    N = int(input())
    X = str(input())

    total = 0
    for index in range(N):
        total += int(X[index])
    
    print(total)