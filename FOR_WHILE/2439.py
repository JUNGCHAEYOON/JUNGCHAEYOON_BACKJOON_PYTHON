# 20220627 정채윤 백준 2439번

if __name__=="__main__":
    N = int(input())

    for index1 in range(N):
        J = index1 + 1
        I = N - J 
        tmp = ""
        for _ in range(I):
            tmp += " "
        for _ in range(J):
            tmp += "*"
        print(tmp)
        
    
