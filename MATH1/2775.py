# 20220709 정채윤 백준 2775번

if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        K = int(input())
        N = int(input())

        # 0층 의 호수별 사람수 배열  
        # 1 2 3 4 5
        people = [X for X in range(1, N + 1)]

        # 1층  
        # 1 3 6 10 15                                      
        for _ in range(K):                  
            for I in range(1, N):
                people[I] += people[I - 1]
            
        print(people[-1])