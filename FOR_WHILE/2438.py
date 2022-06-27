# 20220627 정채윤 백준 2438번

if __name__=="__main__":
    N = int(input())

    for i in range(N):
        tmp = ""
        for j in range(i + 1):
            tmp += "*"
        print(tmp)
        
    
