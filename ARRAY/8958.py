# 20220628 정채윤 백준 1546번

if __name__=="__main__":
    N = int(input())

    for _ in range(N):
        tmp = input()

        point = 0   # 점수
        conti = 0   # 연속된 횟수
        for index in range(len(tmp)):
            if (tmp[index] == 'O'):
                point += 1 + conti
                conti += 1
            elif(tmp[index] == 'X'):
                conti = 0
    
        print(point)